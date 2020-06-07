from django.shortcuts import render
from django.db import models
from news.models import Post


# Create your views here.
def  main(request):
	object_list_3 = Post.objects.all().order_by('-date')[:3]
	return render(request, 'main/index.html', {'posts': object_list_3})