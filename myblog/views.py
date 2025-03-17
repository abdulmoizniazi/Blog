from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView, 
                                  UpdateView, 
                                  DeleteView)


# from django.http import HttpResponse

# Create your views here.

# posts = [
#     {
#         'author': 'Juan',
#         'title': 'Economia de la Argentina',
#         'content': 'lorem ipsum .......',
#         'date_posted': 'August 1, 2044'
#     },
#     {
#         'author': 'Augustina',
#         'title': 'Inmigracion en la Europa',
#         'content': 'lorem ipsum .......',
#         'date_posted': 'August 1, 2077'
#     },
# ]

def home(request):
    # return HttpResponse('<h1>this is HOME page</h1>')
    context = {
        # 'posts': posts,
        'posts': Post.objects.all(),
    }
    return render(request, 'myblog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'myblog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2


class UserPostListView(ListView):
    model = Post
    template_name = 'myblog/user_posts.html'
    context_object_name = 'posts'
    # ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
 

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    

def about(request):
    # return HttpResponse('<h1>this is ABOUT page</h1>')

    return render(request, 'myblog/about.html', {'title': 'About'}) 