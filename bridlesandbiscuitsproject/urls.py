"""
URL configuration for bridlesandbiscuitsproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bookingstablestays.views import IndexView, FacilitiesView, BookingView, ReviewListView, BookingListView, AddReviewView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("accounts/", include("allauth.urls")),
    path('facilities/', FacilitiesView.as_view(), name='facilities'),
    path('book/', BookingView.as_view(), name='book'),
    path('bookings/', BookingListView.as_view(), name='yourbookings'),
    path('reviews/', ReviewListView.as_view(), name='reviews'),
    path('add_review/', AddReviewView.as_view(), name='add_review'),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')), 
    path('bookingstablestays/', include('bookingstablestays.urls')),  # Include the app urls here
]