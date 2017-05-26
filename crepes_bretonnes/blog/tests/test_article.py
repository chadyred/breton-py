from django.test import TestCase
from datetime import datetime, timedelta
from blog.models import Article

class ArticleTests(TestCase):
    def setUp(self):
        """Avant chaque test"""

        print("setUp")

    @classmethod
    def setUpTestData(cls):
        """Avant tout les test, avec une mise en commun"""
        print("setUpDataTest")

    def test_article_date_value_request_equal(self):
        """
        Check good date value.
        """
        date = datetime.now() + timedelta(days=100)
        article = Article(date=date)

        day = 12
        add_day = 10
        date = datetime(2016, 2, day) + timedelta(days=10)
        article = Article(date=date)

        self.assertEqual(article.date, datetime(2016, 2, (day + add_day)))

        day = 31
        take_off_day = 30
        date = datetime(2016, 12, day) - timedelta(days=take_off_day)
        article = Article(date=date)

        self.assertEqual(article.date, datetime(2016, 12, (day - take_off_day)))

    def test_article_recent_correspond(self):
        """
        Véfirifie si la méthode est_recent de l'article retourne bien
        true si l'article est assez récent
        """
        futur_article = Article(date=datetime.now() + timedelta(days=100))

        self.assertEqual(futur_article.is_recent(),True)

    def test_article_non_recent_correspond(self):
        """
        Véfirifie si la méthode est_recent de l'article retourne bien
        true si l'article est assez récent
        """
        futur_article = Article(date=datetime.now() - timedelta(days=100))

        self.assertEqual(futur_article.is_recent(),False)