from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.contrib import messages

STATUS = ((0, "unbooked"), (1, "booked"))


# Create your models here.
class Stables(models.Model):
    stable_num = models.IntegerField(unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    cost_per_night = models.DecimalField(max_digits=6, decimal_places=2, default=150)  # noqa


class Stable_availability(models.Model):
    stable = models.ForeignKey(Stables, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


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
    stable_id = models.ForeignKey(Stables, on_delete=models.CASCADE, related_name="bookings")  # noqa

    class Meta:
        ordering = ["-booked_on"]

    def __str__(self):
        return f"{self.horse_name} | booked by {self.user.username}"


class Review(models.Model):
    """
    Stores a single review entry related to :model:`auth.User` and :model:`Book`.  # noqa
    """
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")  # noqa
    rating = models.IntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(5)
    ])
    comment = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    bookingid = models.ForeignKey('Book', on_delete=models.CASCADE, related_name="reviews")  # noqa

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.rating} - {self.comment[:20]} by {self.user.username}"  # noqa
