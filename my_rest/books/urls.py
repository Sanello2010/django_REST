from django.urls import path
from . import views

urlpatterns = [
    path("showbooks/", views.ShowBooks.as_view(), name="showbooks_url"),
    path("showgenres/", views.ShowGenre.as_view(), name="showgenres_url"),

]