from django.urls import reverse
from rest_framework import status

from apps.shared.BaseTest import BaseTest


class ApartmentTest(BaseTest):
    list = 'apps.apartment:apartment-list'

    def test_list(self):
        response = self.client.get(reverse(self.list))
        self.assertEqual(
            response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(response.data.get('count'), 11)

    def test_filtered_list(self):
        query = dict(
            min_price=1000000,
            max_price=3000000,
            start_floor=2,
            last_floor=20,
            rooms='1,2,3',
            not_first_last=True
        )
        response = self.client.get(reverse(self.list), query)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK, response.data)
        for item in response.data.get('results'):
            self.assertLessEqual(item['price'], query['max_price'])
            self.assertGreaterEqual(item['price'], query['min_price'])
            self.assertLessEqual(item['floor'], query['last_floor'])
            self.assertGreaterEqual(item['floor'], query['start_floor'])
            self.assertNotEqual(item['floor'], 1)
            self.assertNotEqual(item['floor'], item['max_floor'])
            self.assertNotIn(item['floor'], query['rooms'].split(','))
