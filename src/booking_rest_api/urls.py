from django.urls import path
from .views import UserApiView, HotelOwnerListView, HotelOwnerDetailView, HobbyListApiView

urlpatterns = [
    path('users/', UserApiView.as_view()),
    path('hotel-owners/', HotelOwnerListView.as_view()),
    path('hotel-owners/<int:pk>/', HotelOwnerDetailView.as_view(), name='hotel_owner_detail'),
    path('hobbies/', HobbyListApiView.as_view(), name='hobbies'),
]