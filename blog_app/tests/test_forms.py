from django.test import TestCase
from blog_app.forms import TopicForm
from blog_app.models import Tag


class TestForms(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name='tag1')
        self.tag2 = Tag.objects.create(name='tag2')
        self.data = {
            'title': 'Test Title',
            'subtitle': 'Test Subtitle',
            'description': 'Test Description',
            'tags': [self.tag1.pk, self.tag2.pk],
        }

    def test_form_valid(self):
        form = TopicForm(data=self.data)
        self.assertTrue(form.is_valid())

        topic = form.save()
        self.assertEqual(topic.title, 'Test Title')
        self.assertEqual(topic.subtitle, 'Test Subtitle')
        self.assertEqual(topic.description, 'Test Description')
        self.assertEqual(topic.tags.count(), 2)

    def test_form_invalid(self):
        form = TopicForm(data={'title': ''})
        self.assertFalse(form.is_valid())
        