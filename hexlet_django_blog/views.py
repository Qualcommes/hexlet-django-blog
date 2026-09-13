from django.shortcuts import render
from django.views.generic import TemplateView

from django.shortcuts import redirect
from django.urls import reverse


def index(request):
    redirect_url = reverse('article:article', kwargs={'tags': 'python', 'article_id': 42})
    return redirect(redirect_url)


def about(request):
    return render(request, "about.html")


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context