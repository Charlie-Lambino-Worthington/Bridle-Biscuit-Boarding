from . import views
from django.urls import path

urlpatterns = [
    path('', views.views.homepage, name='home'),
    path('facilities/', views.facilities, name='facilities'),
    path('book/', views.Booking.as_view(), name='Booking'),
    path('reviews/', views.reviewlist.as_view(), name='reviewlist'),
    path('yourbookings/', views.YourBooking.as_view(), name='YourBookings'),
]