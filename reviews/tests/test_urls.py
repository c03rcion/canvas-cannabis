from django.urls import reverse, resolve


class TestUrls:
    def test_strain_detail_url(self):
        path = reverse('reviews:strain_detail', kwargs={'id': 3})
        assert resolve(path).view_name == 'reviews:strain_detail'