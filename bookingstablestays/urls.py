from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('facilities/', views.facilities, name='facilities'),
    path('book/', views.Booking, name='Booking'),
    path('reviews/', views.reviewlist, name='reviewlist'),
    path('yourbookings/', views.YourBooking, name='YourBookings'),
]