from django.shortcuts import render, HttpResponse

def about(request):
    return HttpResponse("hi there! i'm Hello World. ")

def home(request):
    return HttpResponse("Home")