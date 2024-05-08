from django.urls import path
from agenda.views import index, show_event

urlpatterns = [
      path("", index),
      path("event", show_event)
]