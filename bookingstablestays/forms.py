from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Review
from .models import Book

# setup datepicker for bookings
class DateInput(forms.DateInput):
    input_type = 'date'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'rating', 'featured_image', 'comment', 'bookingid')
        labels = {
            "title": "Review heading",
            "rating": "Rating out of five",
            "featured_image": "Upload image",
            "comment": "Review",
            "bookingid": "Booking ID",
        }
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 0 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating

class EditForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'rating',  'comment', )
        labels = {
            "title": "Review heading",
            "rating": "Rating out of five",
            "comment": "Review",
        }
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 0 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('horse_name', 'feeding_requirements', 'exercise_requirements', 'stay_start', 'stay_end', 'number_nights', 'email')
        # set date fields to use datepicker
        widgets = {
            'stay_start': DateInput(),
            'stay_end': DateInput(),
        }
        labels = {
            "horse_name": "Horse or donkey's name",
            "feeding_requirements": "Feeding requirements",
            "exercise_requirements": "Exercise requirements",
            "stay_start": "Booking start date",
            "stay_end": "Booking end date",
            "number_nights": "Number of nights",
            "email": "Email address",
        }
   