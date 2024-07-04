from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.contrib import messages

STATUS = ((0, "unbooked"), (1, "booked"))

# Create your models here.
class stables(models.Model):
    stable_num = models.IntegerField(default=10)
    status = models.IntegerField(choices=STATUS, default=0)
    cost_per_night = models.DecimalField(max_digits=5, decimal_places=2, default=150)

class stable_availability(models.Model):
    stable = models.ForeignKey(stables)
    start_date = models.DateField()
    end_date = models.DateField

class Book(models.Model):
    """
    Stores a single booking entry related to :model:`auth.User`.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="book_posts"
    )
    horse_name = models.CharField(max_length=200)
    feeding_requirements = models.TextField()
    exercise_requirements = models.TextField()
    stay_start = models.DateField()
    stay_end = models.DateField()
    number_nights = models.IntegerField()
    booked_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    bookingid = models.SlugField(max_length=200, unique=True)
    email = models.EmailField()
    cost = models.ForeignKey(stables.costpernight) * self.number_nights
    stable_id = models.ForeignKey(Stables, on_delete=models.CASCADE, related_name="bookings")

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.horse_name} | written by {self.userid}"

class Review(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`.
    """
    title = models.CharField(max_length=200)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    rating = models.IntegerField(default=0)
    comment = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    bookingid = Book.bookingid

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"review {self.rating, self.comment, self.featured_image, self.created_on} by {self.author}"