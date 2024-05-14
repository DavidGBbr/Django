from django.urls import path
from agenda.views import get_events, show_event

urlpatterns = [
      path("", get_events),
      path("events/<int:id>/", show_event)
]