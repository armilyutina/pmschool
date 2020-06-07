from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from news.models import Post
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.news, name = 'news'),
    path('<pk>', DetailView.as_view(model = Post, template_name = 'news/artical.html')),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
