from . import views
from django.urls import path

urlpatterns = [
    path('bookings/', views.BookingListView.as_view(), name='yourbookings'),
    path('reviews/', views.ReviewListView.as_view(), name='reviews'),
    path('review_edit/<int:review_id>/', views.review_edit, name='review_edit'),  # noqa
    path('delete_booking/<str:booking_id>/', views.booking_delete, name='delete_booking'),  # noqa
]
