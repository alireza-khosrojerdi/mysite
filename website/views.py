from django.shortcuts import render, HttpResponse
from website.forms import ContactForm 
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            a = form.save()
            a.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submitted successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt submitted')

    form = ContactForm()
    return render(request, 'website/index.html' ,{'form':form})


def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            a = form.save()
            a.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submitted successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt submitted')

    form = ContactForm()
    return render(request, 'website/about.html',{'form':form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            a = form.save()
            a.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submitted successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt submitted')

    form = ContactForm()
    return render(request, 'website/contact.html',{'form':form})




def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
    form = ContactForm()
    return render(request, 'test.html', {'form': form})
