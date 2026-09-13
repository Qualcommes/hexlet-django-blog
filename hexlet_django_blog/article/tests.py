from django.test import TestCase
from django.urls import reverse
from hexlet_django_blog.article.factories import ArticleFactory

# Create your tests here.
class ArticleTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем 20 статей фабрикой
        cls.articles = ArticleFactory.create_batch(20)

    def test_articles_list_view(self):
        url = reverse("article:articles")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        # Проверяем, что на первой странице ровно 15 статей (из-за paginate_by = 15)
        self.assertEqual(len(response.context["articles"]), 15)
        # Проверяем наличие page_obj в контексте
        self.assertIn("page_obj", response.context)

    def test_articles_list_second_page(self):
        url = reverse("article:articles")
        response = self.client.get(f"{url}?page=2")

        self.assertEqual(response.status_code, 200)
        # На второй странице оставшиеся 5 статей
        self.assertEqual(len(response.context["articles"]), 5)
        self.assertEqual(response.context["page_obj"].number, 2)