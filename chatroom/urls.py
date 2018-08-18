from django.urls import path
import chatroom.views as views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'conversations', views.ConverstionViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'messages', views.MessageViewSet)

urlpatterns = router.urls