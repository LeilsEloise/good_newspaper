from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from .models import Article, Comment
from .forms import CommentForm


class ArticleList(generic.ListView):
    queryset = Article.objects.filter(status=1).order_by("-created_on")
    template_name = "newstories/index.html"
    paginate_by = 6


def article_detail(request, slug):
    queryset = Article.objects.filter(status=1)
    article = get_object_or_404(queryset, slug=slug)
#ChatGPT Unapproved Comments Code
    if request.user.is_authenticated:
        comments = article.comments.filter(
            Q(approved=True) | Q(author=request.user)
        ).order_by("-created_on")
    else:
        comments = article.comments.filter(
            approved=True
        ).order_by("-created_on")

    comment_count = article.comments.filter(approved=True).count()
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.save()
            messages.success(
                request,
                "Comment submitted and awaiting approval"
            )
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