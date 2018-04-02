from django.urls import reverse_lazy
from django.views.generic import \
    ListView, \
    DetailView, \
    CreateView, \
    UpdateView, DeleteView

from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'post_edit.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')