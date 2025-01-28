from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import XAccount

class LatestPostsViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a test XAccount for the tests
        self.test_account = XAccount.objects.create(
            username="test_user",
            latest_post_id="12345"
        )

    def test_latest_posts(self):
        """
        Test that the latest-posts endpoint returns a 200 status code.
        """
        response = self.client.get(reverse('latest-posts'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_latest_posts_with_data(self):
        """
        Test that the latest-posts endpoint returns the correct data.
        """
        response = self.client.get(reverse('latest-posts'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("latest_post_id", response.data)
        self.assertEqual(response.data["latest_post_id"], self.test_account.latest_post_id)