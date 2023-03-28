from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from News.views import home,onSubmit

class TestUrls(SimpleTestCase):
    def test_home_urls_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func,home)
        def test_home_urls_is_resolved(self):
        url = reverse('Output')
        print(resolve(url))
        self.assertEquals(resolve(url).func,onSubmit)
