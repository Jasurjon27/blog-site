from django.shortcuts import render
from models import Category,Tag,Author,Post
# Create your views here.


def home_page(request):
    posts = Post.objects.all().order_by('-id')[:6]
    context = {'posts':posts}
    return render(request,'index.html', context)
