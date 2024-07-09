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
from django.utils.text import slugify
import random
import uuid  # Import uuid module for generating UUIDs

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

class FacilitiesView(TemplateView):
    template_name = "facilities.html"

class ReviewListView(generic.ListView):
    model = Review
    template_name = "reviews.html"
    paginate_by = 6

    def get_queryset(self):
        return Review.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        return context

    @login_required
    def add_review(self, request):
        """Add review"""
        if request.method == 'GET':
            """What happens for a GET request"""
            return render(request, "reviews.html", {"review_form": ReviewForm()})

        if request.method == 'POST':
            """What happens for a POST request"""
            review_form = ReviewForm(request.POST, request.FILES)

            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.user = request.user
                review.save()
                return redirect('reviews')
            else:
                messages.error(request, 'Please complete all required fields')
                review_form = ReviewForm()

            return render(
                request,
                "reviews.html",
                {"review_form": review_form}
            )
    
    """review(self, request, *args, **kwargs):
        form = ReviewForm(request.Review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            messages.add_message(request, messages.SUCCESS, 'New review created!')
            return redirect("reviews.html")
        else:
            messages.add_message(request, messages.ERROR, 'Error creating review.')
            return self.get(request, *args, **kwargs) """

class BookingListView(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name = "yourbookings.html"
    paginate_by = 2
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)
    
    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookForm()
        return context"""


class CheckAvailabilityMixin:
    def check_stable_availability(self, stay_start, stay_end):
        now = timezone.now().date()

        if stay_start < now:
            messages.error(self.request, "Check-in date is not valid. Please enter a valid date.")
            return False

        if stay_end <= stay_start:
            messages.error(self.request, "Check-out date is not valid. Please enter a valid date.")
            return False

        # Query to find overlapping bookings for the same stable
        overlapping_bookings = Book.objects.filter(
            Q(stay_start__lte=stay_end, stay_end__gte=stay_start) |
            Q(stay_start__range=(stay_start, stay_end))
        )

        # Get all stables and exclude those with overlapping bookings
        available_stables = Stables.objects.exclude(id__in=overlapping_bookings.values_list('stable_id', flat=True))

        return available_stables if available_stables.exists() else False

"""
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
        Book.user = self.request.user
        Book.save()
        messages.success(self.request, 'Booking successful!')
        return super().form_valid(form)
 """
class BookingView(LoginRequiredMixin, CheckAvailabilityMixin, View):
     """What happens for a GET request"""
     def get(self, request):
    #add booking
        return render(
            request, "book.html", {"bookform": BookForm()})

     def post(self, request):
        """What happens for a POST request"""
        print(request.POST)
        book_form = BookForm(request.POST, request.FILES)

        if book_form.is_valid():
            stay_start = book_form.cleaned_data['stay_start']
            stay_end = book_form.cleaned_data['stay_end']

             # Query all stables
            all_stables = Stables.objects.all()
            
            available_stables = self.check_stable_availability(stay_start, stay_end)

            if not available_stables:
                messages.error(request, 'No available stables for the selected dates.')
                return render(request, "book.html", {"bookform": book_form})

            selected_stable = random.choice(available_stables)
            print(selected_stable)
            print(f"Selected stable ID: {selected_stable.id}")
            booking = book_form.save(commit=False)
            booking.user = request.user
            booking.stable_id = selected_stable
            # Generate random booking ID
            booking.bookingid = uuid.uuid4().hex[:12].lower()  # Generate a random 12-character hex string
            
            booking.save()
            return redirect('yourbookings')
        else:
            print("Form errors:", book_form.errors.as_data())
            messages.error(request, 'Please complete all required fields')
            book_form = BookForm()

        return render(
            request,
            "book.html",
            {
                "bookform": book_form

            },
        )
