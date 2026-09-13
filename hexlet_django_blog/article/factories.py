import factory
from hexlet_django_blog.article.models import Article


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    name = factory.Faker("sentence", nb_words=4)
    body = factory.Faker("paragraph")