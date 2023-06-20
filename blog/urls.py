from django.urls import path
from blog.views import *
from blog.feeds import LatestEntriesFeed

app_name = 'blog'

urlpatterns = [
    path('', blog, name='blog'),
    path('<int:pid>', blog_single, name='single'),
    path('category/<str:cat_name>', blog, name='category'),
    path('tag/<str:tag_name>', blog, name='tag'),
    path('author/<str:author_username>', blog, name='author'),
    path('search/',blog_search, name='search'),
    path('test', test, name='test'),
    path('rss/feed/', LatestEntriesFeed())

]
