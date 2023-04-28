from django.shortcuts import render

# Create your views here.


def blog(request):
    return render(request, 'blog/blog-home.html')


def blog_single(request):
    context = {'title': 'bitcoin crashed again!',
               'content': 'bitcoin was flying but now grounded as allways'}
    return render(request, 'blog/blog-single.html', context)
