from django import forms
from .models import Review
from .models import Book

# setup datepicker for bookings
class DateInput(forms.DateInput):
    input_type = 'date'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'rating', 'featured_image', 'comment', 'bookingid')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('horse_name', 'feeding_requirements', 'exercise_requirements', 'stay_start', 'stay_end', 'number_nights', 'email')
        # set date fields to use datepicker
        widgets = {
            'stay_start': DateInput(),
            'stay_end': DateInput(),
        }
   