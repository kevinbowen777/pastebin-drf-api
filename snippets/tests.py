from django.contrib.auth import get_user_model
from django.urls import reverse  # noqa:F401
from rest_framework import status  # noqa:F401
from rest_framework.test import APITestCase

from .models import Snippet


class SnippetTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="blogreader", password="T3stP@s5123"
        )

        cls.snipp = Snippet.objects.create(
            owner=cls.user,
            title="Snippet title",
            code="print('Hello World')",
            linenos=False,
            language="python",
            style="friendly",
        )

    def test__str__(self):
        snippet = Snippet.objects.get(id=1)
        assert snippet.__str__() == snippet.title
        assert str(snippet) == snippet.title

    """
    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        body = f"{post.body}"
        self.assertEqual(author, "blogreader")
        self.assertEqual(title, "Blog title")
        self.assertEqual(body, "Nice Body content...")

    def test_api_listview(self):
        self.client.login(username="blogreader", password="T3stP@s5123")
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)
        # self.assertContains(response, self.post)

    def test_api_logged_out_deny_listview_access(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_detailview(self):
        self.client.login(username="blogreader", password="T3stP@s5123")
        response = self.client.get(
            reverse("post_detail", kwargs={"pk": self.post.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)
        self.assertContains(response, "Nice Body content...")
    """
