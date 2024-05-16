from django.urls import path
from .views import index, hotels, users, comments, hotels_view, persons

urlpatterns = [
    path('index', index, name="index"),
    path('hotels', hotels, name="hotels"),
    path('users', users, name="users"),
    path('comments', comments, name="comments"),
    path('persons', persons, name="persons"),
    path('hotels_view', hotels_view, name="hotels_list_view"),]
