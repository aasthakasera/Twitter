from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Tweet(models.Model):
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL,default=1, null=True, on_delete=models.SET_NULL)
	title 		= models.CharField(max_length=120)
	content 	= models.TextField(null=True, blank=True)
	updated 	= models.DateTimeField(auto_now=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)

