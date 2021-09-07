
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Sport

class PostModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='mohammad',password='pass')
        test_user.save()

        test_post = Sport.objects.create(
            author = test_user,
            title = 'good player',
            sport = 'football'
        )
        test_post.save()

    def test_sport_content(self):
        post = Sport.objects.get(id=1)

        self.assertEqual(str(post.author), 'mohammad')
        self.assertEqual(post.title, 'good player')
        self.assertEqual(post.sport, 'football')


class APITest(APITestCase):
    def test_auth_list(self):
        response = self.client.get(reverse('sport_list'))
        self.assertEqual(response.status_code, 401)