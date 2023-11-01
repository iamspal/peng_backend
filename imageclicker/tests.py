from django.test import TestCase
from django.urls import reverse
from .models import Gif

class GifViewsTest(TestCase):
    def setUp(self):
        # Create some test Gif objects for testing
        self.gif1 = Gif.objects.create(title="Gif 1", url="http://example.com/gif1.gif", votes=0)
        self.gif2 = Gif.objects.create(title="Gif 2", url="http://example.com/gif2.gif", votes=0)

    def test_index_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'data')
        self.assertContains(response, 'Gif 1')
        self.assertContains(response, 'Gif 2')

    def test_vote_gif_view(self):
        url = reverse('vote_gif')
        initial_votes = self.gif1.votes
        data = {'id': self.gif1.id}
        response = self.client.post(url, data)
        updated_gif = Gif.objects.get(id=self.gif1.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_gif.votes, initial_votes + 1)

    def test_vote_gif_view_invalid_method(self):
        url = reverse('vote_gif')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)

    def test_vote_gif_view_nonexistent_gif(self):
        url = reverse('vote_gif')
        data = {'id': 9999}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 404)