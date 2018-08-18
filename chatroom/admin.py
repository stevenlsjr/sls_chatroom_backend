from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'conversation', 'timestamp', 'content')

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'host')