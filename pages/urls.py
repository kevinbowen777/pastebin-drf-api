from django.urls import path
from snippets.views import SnippetListView

from .views import AboutPageView, HomePageView


urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
    path("snippets/", SnippetListView.as_view(), name="snippetlist"),
]
