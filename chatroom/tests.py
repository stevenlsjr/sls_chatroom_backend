from rest_framework.test import (APIClient, APIRequestFactory, APITestCase)
from django.urls import reverse
from .models import *
from django.contrib.auth.models import User

class TestMessage(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('bob')
        cls.message = Message.objects.create(user=cls.user, content='hello')

    def test_message_list(self):
        self.client.force_login(self.user)
        res = self.client.get(reverse('message-list'))
        assert res.status_code >=200 and res.status_code < 300
        messages = res.data['results']
        find_user = [m for m in messages if m['id'] == self.message.pk]
        assert len(find_user) == 1
    
    