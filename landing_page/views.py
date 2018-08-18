from django.shortcuts import render

from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def index(request, *args, **kwargs):
    context = {
        'admin_url': '/admin/',
        'api_root_url': reverse('chatroom:api-root'),
        'user': request.user,
        'logout_url': reverse('logout')
    }
    return render(request, 'landing_page/index.html', context)