from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'conversation', 'timestamp', 'content')


class MessageAdminInline(admin.TabularInline):
    model = Message
    def get_ordering(self,request):
        return ['timestamp', 'pk']

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    fields = ('title', 'desc', 'host')
    inlines = (MessageAdminInline,)
    list_display = ('title', 'host')