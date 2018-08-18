from rest_framework.test import (APIClient, APIRequestFactory, APITestCase)
from rest_framework import status
from django.urls import reverse
from .models import *
from django.contrib.auth.models import User


class TestMessage(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('bob')
        cls.superuser = User.objects.create_superuser(
            'steve', email='steve@example.com', password='guest')
        cls.message = Message.objects.create(user=cls.user, content='hello')

    def setUp(self):
        self.client.force_login(self.user)

    def test_message_list(self):
        res = self.client.get(reverse('chatroom:message-list'))
        assert res.status_code == status.HTTP_200_OK
        messages = res.data['results']
        find_user = [m for m in messages if m['id'] == self.message.pk]
        assert len(find_user) == 1

    def test_message_create(self):
        data = {'content': 'hello everyone!!!', 'user': self.user.id}
        res = self.client.post(reverse('chatroom:message-list'), data=data)
        assert res.status_code == status.HTTP_201_CREATED
        assert Message.objects.get(content='hello everyone!!!')

    def test_message_delte(self):
        pk = self.message.pk
        res = self.client.delete(reverse('chatroom:message-detail', kwargs={'pk': self.message.id}))
        assert res.status_code == status.HTTP_204_NO_CONTENT
        assert Message.objects.filter(pk=pk).count() == 0
