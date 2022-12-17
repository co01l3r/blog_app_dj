from django.test import TestCase
from blog_app.models import Topic, Tag


class TestModels(TestCase):

    def setUp(self):
        self.tag1 = Tag.objects.create(name='tag1')
        self.tag2 = Tag.objects.create(name='tag2')
        self.topic = Topic.objects.create(
            title='Test Title',
            subtitle='Test Subtitle',
            description='Test Description',
        )
        self.topic.tags.set([self.tag1, self.tag2])

    def test_topic_str(self):
        self.assertEqual(str(self.topic), 'Test Title')

    def test_tag_str(self):
        self.assertEqual(str(self.tag1), 'tag1')
        self.assertEqual(str(self.tag2), 'tag2')

    def test_topic_tags(self):
        self.assertEqual(self.topic.tags.count(), 2)
        self.assertIn(self.tag1, self.topic.tags.all())
        self.assertIn(self.tag2, self.topic.tags.all())
