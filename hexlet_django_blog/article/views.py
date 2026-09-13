from django.shortcuts import render
from django.views import View
from hexlet_django_blog.article.models import Article
from django.views.generic import ListView
from django.http import HttpResponse


def index(request, tags, article_id):
    return HttpResponse(f"Статья номер {article_id}. Тег {tags}")

class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'articles/main_view.html',
            context={'app_name': 'hexlet-django-blog'},
        )

class ArticleListView(ListView):
    model = Article
    paginate_by = 15
    context_object_name = "articles"