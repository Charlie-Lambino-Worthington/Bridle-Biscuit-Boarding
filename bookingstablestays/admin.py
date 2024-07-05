from django.contrib import admin
from .models import Book, Stables, Stable_availability, Review
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Book, Review, Stables, Stable_availability )
class PostAdmin(SummernoteModelAdmin):

    list_display = ('horse_name', 'status', 'created_on')
    search_fields = ['horse_name', 'bookingid']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'bookingid': ('horse_name','created_on')}
    summernote_fields = ('feeding_requirements', 'exercise_requirements')


# Register your models here.
admin.site.register(Book, Review, Stables, Stable_availability)