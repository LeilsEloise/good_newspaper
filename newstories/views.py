from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Article

# Create your views here.
class ArticleList(generic.ListView):
    queryset = Article.objects.filter(status=1).order_by("-created_on")
    template_name = "newstories/index.html"
    paginate_by = 6

def article_detail(request, slug):
    """
    Display an individual :model:`newstories.Article`.

    **Context**

    ``post``
        An instance of :model:`newstories.Article`.

    **Template:**

    :template:`newstories/article_detail.html`
    """

    queryset = Article.objects.filter(status=1)
    article = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "newstories/article_detail.html",
        {"article": article },
    )