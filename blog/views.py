from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post

# Create your views here.

def blog(request, **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    less = Post.objects.filter(status=1, pk__lt=pid)[:1]
    more = Post.objects.filter(status=1, pk__gt=pid).reverse()[:1]
    post.counted_view += 1
    post.save()
    context = {'post': post, 'less': less, 'more': more}
    return render(request, 'blog/blog-single.html', context)


def test(reqeuest):
    return render(reqeuest, 'test.html')


def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        # print(request.GET.get('s'))
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
