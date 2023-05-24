from django.shortcuts import render, get_object_or_404
from blog.models import Post
import datetime
# Create your views here.


def blog(request):
    date = datetime.datetime.now()
    posts = Post.objects.filter(published_date__lte=date)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request , pid):
    post = get_object_or_404(Post, pk=pid)
    post.counted_view += 1
    post.save()
    context = {'post': post}
    return render(request, 'blog/blog-single.html',context)


def test(reqeuest, pid):
    # post = Post.objects.get(id = pid)
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post}
    return render(reqeuest, 'test.html', context)
