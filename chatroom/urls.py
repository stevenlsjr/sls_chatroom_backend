from django.urls import path, re_path
import chatroom.views as views

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register(r'conversations', views.ConverstionViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'messages', views.MessageViewSet)

app_name = 'chatroom'

urlpatterns = [
    re_path(r'api-token-auth/$', obtain_auth_token)
]

urlpatterns += router.urls
