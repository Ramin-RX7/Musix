from typing import Any, Dict
from django.http import HttpResponse,Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from ..models import User



class ProfileView(DetailView):
    model = User
    template_name = "accounts/profile.html"
    pk_url_kwarg='username'
    context_object_name='user'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["playlists"] = self.object.playlist_set.all()
        print(context["playlists"])
        return context


    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        username = self.kwargs.get(self.pk_url_kwarg)
        try:
            obj = queryset.get(username=username)
            if obj.is_staff and (not self.request.user.is_staff):
                raise queryset.model.DoesNotExist
        except queryset.model.DoesNotExist:
            raise Http404(
                ("No %(verbose_name)s found matching the query")
                % {"verbose_name": queryset.model._meta.verbose_name}
            )
        return obj
