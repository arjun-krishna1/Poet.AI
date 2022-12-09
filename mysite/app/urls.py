from django.urls import path

from .views import index, visualizeTranscript

urlpatterns = [
  path("", index, name="index"),
  path("visualizeTranscript/", visualizeTranscript, name="visualizeTranscript"),
]
