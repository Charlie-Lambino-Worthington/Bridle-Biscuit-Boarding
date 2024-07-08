from django import forms
from .models import Review
from .models import Book

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'rating', 'featured_image', 'comment', 'bookingid')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('horse_name', 'feeding_requirements', 'exercise_requirements', 'stay_start', 'stay_end', 'number_nights', 'email','stable_id',)

   
    
    
 
 
