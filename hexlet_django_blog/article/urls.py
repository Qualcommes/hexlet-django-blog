from django.urls import path
from hexlet_django_blog.article.views import ArticleListView
from hexlet_django_blog.article import views

app_name = 'article'

urlpatterns = [
    path("", ArticleListView.as_view(), name="articles"),
    path('<str:tags>/<int:article_id>/', views.index, name='article'),
]