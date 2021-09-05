from django.shortcuts import render
from django.views.generic import ListView , DetailView  
from .models import Post, Comment
from django.views import View

# Create your views here.

class NewsList(ListView):
  model = Post
  template_name = 'news.pug'
  context_object_name = 'news'
  queryset = Post.objects.order_by('-dateCreated')


class PostView(DetailView):
  model = Post
  template_name = 'post.pug'
  context_object_name = 'post'

# class CommentView(DetailView):
#   model = Comment
#   template_name = 'comment.pug'
#   context_object_name = 'comment'

class HomePageView(View):
  template_name = "index.pug"