from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def news_story(request):
    return HttpResponse("What's new?")