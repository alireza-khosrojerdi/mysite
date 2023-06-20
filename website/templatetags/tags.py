from django import template
from blog.models import Post

register = template.Library()


@register.filter
def snippet(value, arg=20):
    return value[:arg] + '...'


@register.inclusion_tag('website/website-latest.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts': posts}

@register.inclusion_tag('website/website-posts.html')
def Summary(arg=3):
    posts = Post.objects.filter(status=1).order_by('-counted_view')[:arg]
    return {'posts': posts}
