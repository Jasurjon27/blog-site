from django.shortcuts import render
from models import Post
# Create your views here.


def home_page(request):
    posts = Post.objects