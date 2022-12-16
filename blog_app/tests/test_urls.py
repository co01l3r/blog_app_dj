from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog_app.views import topics, topic, topic_create_or_update, topic_delete


class TestUrls(SimpleTestCase):

    def test_topics_url_resolves(self):
        url = reverse('topics')
        self.assertEquals(resolve(url).func, topics)

    def test_topic_url_resolves(self):
        url = reverse('topic', args=['1'])
        self.assertEquals(resolve(url).func, topic)

    def test_new_url_resolves(self):
        url = reverse('new')
        self.assertEquals(resolve(url).func, topic_create_or_update)

    def test_update_url_resolves(self):
        url = reverse('update', args=['1'])
        self.assertEquals(resolve(url).func, topic_create_or_update)

    def test_delete_url_resolves(self):
        url = reverse('delete', args=['1'])
        self.assertEquals(resolve(url).func, topic_delete)
