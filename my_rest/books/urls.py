from django.urls import path
from . import views

urlpatterns = [
    path("showbooks/", views.ShowBooks.as_view(), name="showbooks_url"),
    path("showgenre/", views.ShowGenre.as_view(), name="showgenre_url"),

]