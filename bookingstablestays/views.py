from django.views import generic
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import book, review
from .forms import BookForm, ReviewForm

from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.

class Reviewlist(LoginRequiredMixin, generic.ListView):
    template_name = "frontend/reviews.html"
    paginate_by = 6
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.Review)
        if form.is_valid():
            review = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.add_message(request, messages.SUCCESS, 'New review created!')
            return redirect("frontend/reviews.html")
        else:
            messages.add_message(request, messages.ERROR, 'Error creating review.')
            return self.get(request, *args, **kwargs)

