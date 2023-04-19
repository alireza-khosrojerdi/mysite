from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse('this is Home page!!!!')


def about(request):
    return HttpResponse('about page')


def contact(request):
    return HttpResponse('contact page ')
