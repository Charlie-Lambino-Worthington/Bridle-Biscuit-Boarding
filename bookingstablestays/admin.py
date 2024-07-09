from django.contrib import admin
from .models import Book, Stables, Stable_availability, Review
from django_summernote.admin import SummernoteModelAdmin

# Custom admin class for the Book model
@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):
    list_display = ('horse_name', 'status', 'booked_on')
    search_fields = ['horse_name', 'bookingid']
    list_filter = ('status', 'booked_on', 'user', 'bookingid')
    summernote_fields = ('feeding_requirements', 'exercise_requirements')

    def save_model(self, request, obj, form, change):
        if not obj.bookingid:
            obj.bookingid = slugify(f"{obj.horse_name}-{obj.booked_on.strftime('%Y%m%d%H%M%S')}")
        super().save_model(request, obj, form, change)

# Custom admin class for the Review model
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'rating', 'created_on')
    search_fields = ['title', 'user__username']
    list_filter = ('rating', 'created_on')

# Custom admin class for the Stables model
@admin.register(Stables)
class StablesAdmin(admin.ModelAdmin):
    list_display = ('stable_num', 'status', 'cost_per_night')
    search_fields = ['stable_num']
    list_filter = ('status',)

# Custom admin class for the StableAvailability model
@admin.register(Stable_availability)
class StableAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('stable', 'start_date', 'end_date')
    search_fields = ['stable__stable_num']
    list_filter = ('start_date', 'end_date')