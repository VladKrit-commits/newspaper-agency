from django.contrib.auth import get_user_model
from django.test import TestCase

from agency.models import Topic, Newspaper


class ModelsTests(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(name="test")
        self.assertRegex(str(topic), topic.name)

    def test_redactor_str(self):
        redactor = get_user_model().objects.create(
            username="test",
            first_name="test_first",
            last_name="test_last",
        )
        self.assertEqual(
            str(redactor),
            f"{redactor.username} ({redactor.first_name} {redactor.last_name})"
        )

    def test_redactor_get_absolute_url(self):
        redactor = get_user_model().objects.create(
            username="test",
            first_name="test_first",
            last_name="test_last"
        )
        self.assertEqual(
            redactor.get_absolute_url(), "/redactors/1/"
        )

    def test_newspaper_str(self):
        topic = Topic.objects.create(name="test")
        redactor = get_user_model().objects.create(
            username="test",
            first_name="test_first",
            last_name="test_last",
        )
        newspaper = Newspaper.objects.create(topic=topic, title="test")
        newspaper.publishers.set([redactor])

        self.assertEqual(str(newspaper), "test")
