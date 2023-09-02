from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.http import Http404
from django.core.exceptions import ValidationError


from .models import Song



class CodeBasedViewMixin:
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


class PlaylistView(CodeBasedViewMixin, DetailView):
    model = Playlist
    template_name = "player/playlist.html"
    context_object_name = "playlist"
