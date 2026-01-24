from django.shortcuts import render
from django.views import generic
from .models import Article

# Create your views here.
class ArticleList(generic.ListView):
    queryset = Article.objects.filter(status=1).order_by("-created_on")
    template_name = "newstories/index.html"
    paginate_by = 6
