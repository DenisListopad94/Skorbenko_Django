from django.urls import path
from .views import (index, hotels, users, user_comments_view, hotels_view, persons, book_room, details_orders_view,
                    user_add, feedback_add, feedbacks_view, CommentTemplateView, comments)

urlpatterns = [
    path('index', index, name="index"),
    path('hotels', hotels, name="hotels"),
    path('users', users, name="users"),
    # path('comments', comments, name="comments"),
    path('persons', persons, name="persons"),
    path('hotels_view', hotels_view, name="hotels_list_view"),
    path('booking_form', book_room, name='book_room'),
    path('details_orders', details_orders_view, name='details_orders'),
    path('user_add', user_add, name='user_add'),
    path('add_feedback', feedback_add, name='add_feedback'),
    path('feedbacks', feedbacks_view, name='feedbacks'),
    path('comments', CommentTemplateView.as_view(), name="comments"),
    ]
