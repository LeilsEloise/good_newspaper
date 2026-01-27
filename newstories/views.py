from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Article
from .forms import CommentForm

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

    comments = article.comments.filter(approved=True).order_by("-created_on")
    comment_count = comments.count()

    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

            # Reset form after successful submit
            comment_form = CommentForm()

    return render(
        request,
        "newstories/article_detail.html",
        {
            "article": article,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )