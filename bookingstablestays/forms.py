from django import forms
from .models import Review
from .models import Book

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'user', 'rating', 'featured_image', 'comment', 'bookingid')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('horse_name', 'user', 'feeding_requirements', 'exercise_requirements', 'staystart', 'stayend', 'number_nights', 'email')

   
    
    
 
 
