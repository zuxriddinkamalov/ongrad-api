from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

TEST_USER = 'test1@example.com'


class AuthTestCase(object):
    _admin = TEST_USER

    def _get_user(self, username):
        return User.objects.get(username=username)

    def _get_token(self, user):
        token = Token.objects.get_or_create(user=user)
        return 'Token ' + token[0].key

    def _auth_admin(self):
        user = self._get_user(self._admin)
        token = self._get_token(user)
        self.client.credentials(HTTP_AUTHORIZATION=token)

    def _unauth(self):
        self.client.credentials()


class BaseTest(APITestCase, AuthTestCase):
    fixtures = [
        'user.yaml',
        'apartment.yaml',
    ]

    def setUp(self):
        self._auth_admin()
