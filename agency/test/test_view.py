from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from agency.models import Newspaper, Topic, Redactor
from agency.forms import (
    RedactorsSearchForm,
    NewspapersSearchForm
)

REDACTOR_URL = reverse("agency:redactors-list")
NEWSPAPER_URL = reverse("agency:newspapers-list")
TOPIC_URL = reverse("agency:topics-list")


class PublicNewspaperTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        redactor = self.client.get(REDACTOR_URL)
        newspaper = self.client.get(NEWSPAPER_URL)
        topic = self.client.get(TOPIC_URL)
        self.assertNotEqual(redactor.status_code, 200)
        self.assertNotEqual(newspaper.status_code, 200)
        self.assertNotEqual(topic.status_code, 200)


class PrivateNewspaperTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123"
        )
        self.client.force_login(self.user)

    def test_retrieve_redactors(self):
        Topic.objects.create(name="Poem")
        Redactor.objects.create(username="Test")
        response = self.client.get(TOPIC_URL)
        self.assertEqual(response.status_code, 200)
        topics = Topic.objects.all()
        self.assertEqual(
            list(response.context["topics_list"]),
            list(topics)
        )
        self.assertTemplateUsed(response, "agency/topics_list.html")


class PrivateAuthorTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password123"
        )
        self.client.force_login(self.user)


class SearchTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username="user", password="test12test"
        )
        self.client = Client()
        self.client.force_login(self.user)

    def test_search_driver_by_username(self):
        Redactor.objects.create(username="user1", years_of_experience="11")
        Redactor.objects.create(username="user2", years_of_experience="12")

        response = self.client.get(
            reverse("agency:redactors-list"), {"username": "user2"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(
            response.context["search_form"],
            RedactorsSearchForm
        )
        self.assertQuerysetEqual(
            response.context["object_list"],
            Redactor.objects.filter(username__icontains="user2"),
        )

    def test_search_newspaper_by_title(self):
        topic = Topic.objects.create(name="Poetry")
        redactor = get_user_model().objects.create(
            username="test user",
            password="Test12test",
            first_name="test_firstname",
            last_name="test_lastname"
        )
        newspaper1 = Newspaper.objects.create(title="Title1", topic=topic)
        newspaper2 = Newspaper.objects.create(title="Title2", topic=topic)
        newspaper1.publishers.set([redactor])
        newspaper2.publishers.set([redactor])

        response = self.client.get(
            reverse("agency:newspapers-list"), {"title": "Title1"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["search_form"], NewspapersSearchForm)
        self.assertQuerysetEqual(
            response.context["object_list"],
            Newspaper.objects.filter(title__icontains="Title1"),
        )
