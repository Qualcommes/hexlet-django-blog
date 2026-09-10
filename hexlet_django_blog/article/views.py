from django.shortcuts import render


def index(request):
    return render(
        request,
        "articles/main_view.html",
        {"app_name": "hexlet-django-blog"}
        )