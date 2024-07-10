from . import views
from django.urls import path 

urlpatterns = [
    path('bookings/', views.BookingListView.as_view(), name='yourbookings'),
    path('reviews/', views.ReviewListView.as_view(), name='reviews'),
    path('edit_review/<str:review_id>/', views.review_edit, name='review_edit'),
    path('delete_review/<str:review_id>/', views.review_delete, name='review_delete'),  
    path('delete_booking/<str:booking_id>/', views.booking_delete, name='delete_booking'),
]