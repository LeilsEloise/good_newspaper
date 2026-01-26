from . import views
from django.urls import path

app_name = 'newstories'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
]