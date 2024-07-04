from django.views import generic
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import book, review
from .forms import BookForm, ReviewForm
from django.db.models import Q

from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.
class homepage():
    return "static/index.html"

class facilities():
    return "static/facilities.html"


class reviewlist(LoginRequiredMixin, generic.ListView):
    template_name = "static/reviews.html"
    paginate_by = 6
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm()
        return context

    def review(self, request, *args, **kwargs):
        form = ReviewForm(request.Review)
        if form.is_valid():
            review = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.add_message(request, messages.SUCCESS, 'New review created!')
            return redirect("frontend/reviews.html")
        else:
            messages.add_message(request, messages.ERROR, 'Error creating review.')
            return self.get(request, *args, **kwargs)

class CheckAvailabilityMixin:
    def check_stable_availability(self, stable, stay_start, stay_end, current_booking=0):
        # Convert dates to datetime objects for comparison
        now = timezone.now().date()
        stay_start = timezone.make_aware(stay_start).date()
        stay_end = timezone.make_aware(stay_end).date()

        # Check if stay_start is greater than or equal to today
        if stay_start < now:
            messages.error(self.request, "Check-in date is not valid. Please enter a valid date.")
            return False

        # Check if stay_end is less than or equal to stay_start
        if stay_end <= stay_start:
            messages.error(self.request, "Check-out date is not valid. Please enter a valid date.")
            return False

        # Query to find overlapping bookings
        overlapping_bookings = Book.objects.filter(
            Q(stay_start__lte=stay_end, stay_end__gte=stay_start) |
            Q(stay_start__range=(stay_start, stay_end))
        ).exclude(id=current_booking)

        if overlapping_bookings.exists():
            messages.error(self.request, "The selected dates are already booked.")
            return False

        return True


class Booking(LoginRequiredMixin, CheckAvailabilityMixin, FormView):
    template_name = "static/book.html"
    def book(self, request, *args, **kwargs):
        form = BookForm(request.Book)

        def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
            self.check_stable_availability(form.cleaned_data['stable'], form.cleaned_data['stay_start'], form.cleaned_data['stay_end'])
        if not self.check_stable_availability(form.cleaned_data['stable'], form.cleaned_data['stay_start'], form.cleaned_data['stay_end']):
            return self.form_invalid(form)
        
        # Save the booking
        booking = form.save(commit=False)
        booking.user = self.request.user
        booking.save()
        messages.success(self.request, 'Booking successful!')
        return super().form_valid(form)