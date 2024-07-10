from django.views import generic, View
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Book, Review, Stables
from .forms import BookForm, ReviewForm
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

class FacilitiesView(TemplateView):
    template_name = "facilities.html"

class ReviewListView( generic.ListView):
    model = Review
    template_name = "reviews.html"
    paginate_by = 6
    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm()
        return context

   
class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        review_form = ReviewForm(request.POST, request.FILES)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, 'Review added successfully.')
            return redirect('reviews')
        else:
            messages.error(request, 'Please complete all required fields')
            return redirect('reviews')

@login_required   
def review_edit(request, review_id):
    """
    Display an individual comment for edit.

    **Context**

    ``Booking``
        An instance of :model:`bookingstablestays.Book`.
    ``Review``
        A single Review related to the Booking.
    ``review_form``
        An instance of :review_form:`bookingstablestays.ReviewForm`
    """
    if request.method == "POST":
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.user == request.user:
            review = review_form.save(commit=False)
            review.save()
            messages.add_message(request, messages.SUCCESS, 'New review created!')
            return redirect("reviews.html")
        else:
            messages.add_message(request, messages.ERROR, 'Error creating review.')
            return self.get(request, *args, **kwargs)

class BookingListView(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name = "yourbookings.html"
    paginate_by = 2
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookForm()
        return context


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


class BookingView(LoginRequiredMixin, CheckAvailabilityMixin, FormView):
    template_name = "book.html"
    def book(self, request, *args, **kwargs):
        form = BookForm

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

def review_delete(request, review_id):
    """Deletes review"""
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    return HttpResponseRedirect(reverse(
        'reviews', args=[review.booking_id]))