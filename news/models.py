from django.db import models
import PIL.Image

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 100)
	date = models.DateTimeField()
	text = models.TextField() 
	slug = models.TextField(max_length = 300)
	img = models.ImageField(upload_to='images/')
	
def __str__(self):
		return self.title

