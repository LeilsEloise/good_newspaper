from django.urls import path
from .views import news_story

urlpatterns = [
    path('', news_story, name='newstories'),
]