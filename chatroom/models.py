from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from django.utils.text import slugify
# Create your models here.
User = get_user_model()


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=256)
    timestamp = models.DateTimeField(default=now)
    conversation = models.ForeignKey(
        'chatroom.Conversation',
        on_delete=models.CASCADE,
        blank=True,
        null=True)

    def __str__(self):
        return f'{self.user} at {self.timestamp}'


class Conversation(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=256, null=True, blank=True)
    desc = models.TextField(max_length=256, null=True, blank=True)
    def __str__(self):
        return f'{self.host}: "{self.title}"'
        
