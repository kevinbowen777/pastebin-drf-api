from django.contrib.auth import get_user_model
from django.urls import reverse  # noqa:F401
from rest_framework import status  # noqa:F401
from rest_framework.test import APITestCase

from .models import Snippet


class SnippetTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="snippet_user", password="T3stP@s5123"
        )

        cls.snippet = Snippet.objects.create(
            owner=cls.user,
            title="Snippet title",
            code="print('Hello World')",
            linenos=False,
            language="python",
            style="friendly",
        )

    def test__str__(self):
        # snippet = Snippet.objects.get(id=1)
        assert self.snippet.__str__() == self.snippet.title
        assert str(self.snippet) == self.snippet.title

    def test_blog_content(self):
        # snippet = Snippet.objects.get(id=1)
        # owner = f"{snippet.owner}"
        # title = f"{snippet.title}"
        # code = f"{snippet.code}"
        # self.assertEqual(self.snippet.owner, "snippet_user")
        # self.assertEqual(self.user, "snippet_user")
        self.assertEqual(self.snippet.title, "Snippet title")
        self.assertEqual(self.snippet.code, "print('Hello World')")

    def test_api_listview(self):
        self.client.login(username="snippet_user", password="T3stP@s5123")
        response = self.client.get(reverse("snippet-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Snippet.objects.count(), 1)
        # self.assertContains(response, self.post)

    """
    def test_api_logged_out_deny_listview_access(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    """

    def test_api_detailview(self):
        self.client.login(username="snippet_user", password="T3stP@s5123")
        response = self.client.get(
            reverse("snippet-detail", kwargs={"pk": self.snippet.id}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Snippet.objects.count(), 1)
        self.assertContains(response, "Hello World")
