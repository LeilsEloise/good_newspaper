from . import views
from django.urls import path, re_path

app_name = 'newstories'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path("<slug:slug>/delete_comment/<int:comment_id>/", views.comment_delete, name="comment_delete",),
    path("<slug:slug>/vote/<int:value>/", views.article_vote, name="article_vote",),
    re_path(r'^(?P<slug>[-\w]+)/vote/(?P<value>-?\d+)/$', views.article_vote, name='article_vote'),
]