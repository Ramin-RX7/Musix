from typing import Any, Dict
from django.db.models.query import QuerySet
from django.views.generic import ListView,DetailView
from django.http import Http404,HttpResponse,HttpRequest
from django.core.exceptions import ValidationError
from django.views import View


from .models import Song,Artist,Playlist,Like
from accounts.models import User



class CodeBasedViewMixin:
    pk_url_kwarg = 'code'
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        try:
            queryset = queryset.filter(code=self.kwargs.get("code"))
            obj = queryset.get()
        except (ValidationError,queryset.model.DoesNotExist):
            raise Http404(
                ("No %(verbose_name)s found matching the query")
                    % {"verbose_name": queryset.model._meta.verbose_name}
            )
        return obj



class SongView(CodeBasedViewMixin, DetailView):
    model = Song
    template_name = "player/song.html"
    context_object_name = 'song'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if isinstance(user, User):
            try:
                like = Like.objects.get(owner=user, song=self.object) and True
            except Like.DoesNotExist:
                like = False
            print(like)
            context["is_liked"] = like
        return context




class PlaylistView(CodeBasedViewMixin, DetailView):
    model = Playlist
    template_name = "player/playlist.html"
    context_object_name = "playlist"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["songs"] = Song.objects.all()
        return context


class LikeView(View):
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if not isinstance(request.user, User):
            return HttpResponse("ERROR")
        return super().dispatch(request, *args, **kwargs)
    def post(self, request):
        song = Song.objects.get(id=request.POST["song_id"])
        like,created = Like.objects.get_or_create(owner=request.user, song=song)
        if not created:
            like.delete()
        return HttpResponse("OK")


class PlaylistListView(ListView):
    model = Playlist
    context_object_name = "playlists"
    template_name = "player/playlists.html"
    ordering = "-updated_at"
    max_objects_count = 60

    def get_queryset(self):
        searched = self.request.GET.get("search")
        if searched and len(searched)>=3:
            print("search")
            queryset = self.model.objects.filter(name__icontains=searched)
        else:
            print("all")
            queryset = self.model._default_manager.all()
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset[:self.max_objects_count]



class SongsListView(ListView):
    model = Song
    context_object_name = "songs"
    template_name = "player/songs.html"
    ordering = ("-published_at", "title")
    paginate_by = 3

    def get_queryset(self):
        searched = self.request.GET.get("search")
        if searched and len(searched)>=3:
            print("search")
            queryset = self.model.objects.filter(name__icontains=searched)
        else:
            print("all")
            queryset = self.model._default_manager.all()
        queryset = queryset.order_by(*(self.ordering))
        return queryset




class ArtistListView(ListView):
    model = Artist
    context_object_name = "artists"
    template_name = "player/artists.html"
    ordering = "-created_at"
    max_objects_count = 60

    def get_queryset(self):
        searched = self.request.GET.get("search")
        if searched and len(searched)>=3:
            print("search")
            queryset = self.model.objects.filter(name__icontains=searched)
        else:
            print("all")
            queryset = self.model._default_manager.all()
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset[:self.max_objects_count]





class ArtistView(CodeBasedViewMixin, DetailView):
    model = Artist
    template_name = "player/artist.html"
    context_object_name = "user"


    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        try:
            queryset = queryset.filter(code=self.kwargs.get("code")).prefetch_related("song_set")
            # print(queryset.values())
            obj = queryset.get()
        except (ValidationError,queryset.model.DoesNotExist):
            raise Http404(
                ("No %(verbose_name)s found matching the query")
                    % {"verbose_name": queryset.model._meta.verbose_name}
            )
        return obj



    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["songs"] = self.object.song_set.all()
        return context
