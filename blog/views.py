from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.shortcuts import render

# Main page of the website
def base(request):
    """
        Returns:
        - html: The main page of the project.
    """
    return render(request, 'base.html')

# New blog post.
class BlogPostCreate(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blogpost_form.html' 
    success_url = reverse_lazy('blog:blogpost_list')

# View that lists all the posts    
class BlogPostList(ListView):
    model = BlogPost
    template_name = 'blogpost_list.html'

# View to delete a post
class BlogPostDelete(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:blogpost_list')
    template_name = 'blogpost_delete.html'
    
# View to update a post
class BlogPostUpdate(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy('blog:blogpost_list')
    template_name = 'blogpost_update.html'