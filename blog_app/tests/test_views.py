from django.test import TestCase, Client
from django.urls import reverse
from blog_app.models import Topic, Tag
from blog_app.forms import TopicForm
from blog_app.views import topic_create_or_update
from django.test import RequestFactory


class TestViews(TestCase):

    def test_topic_list_get(self):
        client = Client()
        url = reverse('topics')
        response = client.get(url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_app/topics.html')

    def test_topic_detail_get(self):
        topic = Topic.objects.create(title='Topic Title', description='Topic Description')
        url = reverse('topic', args=[topic.pk])
        client = Client()
        response = client.get(url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_app/topic.html')
        self.assertContains(response, 'Topic Title')
        self.assertContains(response, 'Topic Description')

    def test_topic_create_or_update_get(self):
        client = Client()
        response = client.get(reverse('new'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_app/topic_form.html')

        self.assertIsInstance(response.context['form'], TopicForm)

    def test_topic_create_or_update_post(self):
        tag = Tag.objects.create(name='Tag 1')

        data = {
            'title': 'Topic Title',
            'description': 'Topic Description',
            'featured_image': '',
            'tags': [tag.pk],
            'new_tags': 'Tag 2, Tag 3',
        }
        client = Client()
        response = client.post(reverse('new'), data)

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse('topics'))

        self.assertTrue(Topic.objects.filter(title='Topic Title').exists())
        self.assertTrue(Tag.objects.filter(name='Tag 1').exists())

    def test_update_existing_topic_post(self):
        factory = RequestFactory()
        url = reverse('update', kwargs={'pk': '1'})
        # Create an existing topic
        existing_topic = Topic.objects.create(
            title='Test Title',
            subtitle='Test Subtitle',
            description='Test Description',
        )

        data = {
            'title': 'Updated Title',
            'subtitle': 'Updated Subtitle',
            'description': 'Updated Description',
        }
        request = factory.post(url, data)
        response = topic_create_or_update(request, pk=existing_topic.pk)

        self.assertEqual(response.status_code, 302)

        updated_topic = Topic.objects.get(pk=existing_topic.pk)
        self.assertEqual(updated_topic.title, 'Updated Title')
        self.assertEqual(updated_topic.subtitle, 'Updated Subtitle')
        self.assertEqual(updated_topic.description, 'Updated Description')

    def test_topic_delete_post(self):
        topic = Topic.objects.create(
            title='Topic Title',
            description='Topic Description',
        )

        client = Client()
        response = client.post(reverse('delete', args=[topic.pk]))

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse('topics'))

        self.assertFalse(Topic.objects.filter(pk=topic.pk).exists())
