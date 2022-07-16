from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import (
    CreateView, 
    UpdateView, 
    DeleteView
)
from .models import Blog    

# Create your views here.

class BlogView(ListView):
    model = Blog
    ordering = '-add_time'
    template_name = "blogs.html"

class OneBlog(DetailView):
    model = Blog
    template_name = "one.html"

class AddBlog(CreateView):
    model = Blog
    template_name = "add.html"
    fields = ["title", "blog"]
    

class UpdateBlog(UpdateView):
    model = Blog
    template_name = "update.html"
    fields = ["title", "blog"]
    
class DeleteBlogView(DeleteView):
    model = Blog
    template_name = 'delete.html'
    success_url = '/'
    
    