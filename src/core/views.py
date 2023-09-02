from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView

from player.models import *


class Index(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context["latest_playlists"] = Playlist.objects.order_by("-updated_at")[:7]
        context["new_songs"] = Song.objects.order_by("-published_at")[:12]
        context["latest_song"] = context["new_songs"][0]
        return context
