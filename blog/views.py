from django.shortcuts import render, get_object_or_404
from blog.models import Post
import datetime
# Create your views here.


def blog(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request , pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid) 
    less = Post.objects.filter(status=1,pk__lt=pid)[:1]
    more = Post.objects.filter(status=1,pk__gt=pid).reverse()[:1]
    post.counted_view += 1
    post.save()
    context = {'post': post,'less':less,'more':more}
    return render(request, 'blog/blog-single.html',context)


def test(reqeuest, pid):
    # post = Post.objects.get(id = pid)
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post}
    return render(reqeuest, 'test.html', context)
