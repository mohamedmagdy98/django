from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
# Create your views here
# def index(request):
#     return render(request,'login.html',)






from django.shortcuts import render, get_object_or_404

from .models import Post, PostImage

def blog_view(request):
    posts = Post.objects.all().order_by('-id')
    paginator = Paginator(posts, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {
    'posts':posts,
    'page_obj': page_obj,
     })

def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'details.html', {
        'post':post,
        'photos':photos,

    })
