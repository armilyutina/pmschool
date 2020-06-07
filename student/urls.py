from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from student.models import Ad
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', ListView.as_view(queryset = Ad.objects.all().order_by('-date')[:8], template_name='student/student.html'), name= 'student'), 
 ]

if settings.DEBUG: # student
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
