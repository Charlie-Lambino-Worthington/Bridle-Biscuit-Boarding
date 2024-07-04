from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "unbooked"), (1, "booked"))

# Create your models here.
class stables(models.Model):
    stable_num = 10
    status = STATUS
    costpernight = 150

class stable_availability(models.Model):
    id = models.IntegerField()
    stable_id = models.ForeignKey(stables.stable_num)
    start_date = models.DateField()
    end_date = models.DateField

class Book(models.Model):
    """
    Stores a single booking entry related to :model:`auth.User`.
    """
    userid = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="book_posts"
    )
    horse_name = models.CharField(max_length=200, unique=True)
    feeding_requirements = models.TextField()
    exercise_requirements = models.TextField()
    staystart = models.DateField()
    stayend = models.DateField()
    number_nights = models.IntegerField()
    booked_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    bookingid = models.SlugField(max_length=200, unique=True)
    email = models.EmailField()
    cost = models.ForeignKey(stables.costpernight * Book.number_nights)
    stable_id = stables.stable_num

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.horse_name} | written by {self.userid}"

class review(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`.
    """
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