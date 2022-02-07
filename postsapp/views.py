from re import template
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
DetailView,
CreateView,
UpdateView,
DeleteView)
# posts= [
#     {
#     'author':'Rick',
#     'title':'Post One',
#     'content': 'First Post',
#     'date_posted':'August 27 2018'
#     },
#     {
#     'author':'Dees',
#     'title':'Post Two',
#     'content': 'Second Post',
#     'date_posted':'August 28 2018'
#     }
# ] 
# Create your views here.
def home(request):
    # return HttpResponse('<h1>Welcome To The Home of Developers </h1>')
    # Rendering templates
    # return render(request,'postsapp/blog.html')
    context={
        # 'posts':posts
          'posts':Post.objects.all()
    }
    # Passing values,variables,dictionaries
    return render(request,'postsapp/blog.html',context)
class PostListView(ListView):
    model=Post
    template_name='postsapp/blog.html'
    context_object_name='posts'
    # Newest to oldest(Desc)
    ordering=['-date_posted']
    # Oldest to newest(Asc)
    # ordering=['date_posted']
    paginate_by=3
class UserPostListView(LoginRequiredMixin,ListView):
    model=Post
    template_name='postsapp/userposts.html'
    context_object_name='posts'
    paginate_by=3
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
class PostDetailView(DetailView):
    model=Post
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post 
    fields=['title','content'] 
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)  
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post 
    fields=['title','content'] 
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)  
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url="/"
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
    
def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    # Rendering templates
    return render(request,'postsapp/about.html',{'title':'About Us'})

# Rendering templates
