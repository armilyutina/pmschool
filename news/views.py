from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post




# Create your views here.
def news(request):
	object_list = Post.objects.all().order_by('-date')
	paginator = Paginator(object_list, 8)
	page = request.GET.get('page')
	try:
	    posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, 
				  'news/news.html',
				  {'page':page,
				  'posts':posts})


