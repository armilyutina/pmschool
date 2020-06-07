from django.db import models
import PIL.Image

# Create your models here.
class Ad(models.Model):
	title = models.TextField(max_length=2) 
	date = models.DateTimeField()
	text = models.TextField(max_length=500) 

