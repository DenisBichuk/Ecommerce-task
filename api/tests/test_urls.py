from django.test import TestCase
from django.urls import reverse
from rest_framework.status import HTTP_401_UNAUTHORIZED


class TestPermissions(TestCase):
    """Example test"""
    def test_statuses(self):
        urls = (
            reverse(
                'api:category-list',
            ),
            reverse(
                'api:category-detail',
                kwargs={'pk': 1}
            ),
            reverse(
                "api:stock-list",
            ),
            reverse(
                "api:stock-detail",
                kwargs={'pk': 1}
            ),
            reverse(
                "api:equipment-list",
            ),
            reverse(
                "api:equipment-detail",
                kwargs={'pk': 1}
            ),
        )
        expected_status = HTTP_401_UNAUTHORIZED
        for url in urls:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, expected_status)
