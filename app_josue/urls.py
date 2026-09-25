from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
   path("", RedirectView.as_view(pattern_name='attractions', permanent=True)),
   path("attractions", views.attractions, name="attractions"),
   path("identity", views.identity, name="identity"),
   path("pictures", views.pictures, name="pictures")
]