from django.conf import settings
from django.db import models
from django.urls import reverse
# from django.core.exceptions import ValidationError
from django.utils import timezone
from .validator import validate_content


class Tweet(models.Model):
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL,default=1, null=True, on_delete=models.SET_NULL)
	title 		= models.CharField(max_length=120, validators=[validate_content])
	content 	= models.TextField(null=True, blank=True)
	updated 	= models.DateTimeField(auto_now=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.title)

	# def get_absolute_url(self):
	# 	return reverse("tweet:detail" kwargs={"pk":self.pk})

	# def clean(self, *args, **kwargs):
	# 	content = self.content
	# 	if content == "abc":
	# 		raise ValidationError("Cannot be ABC")
	# 	return super(Tweet, self).clean(*args, **kwargs)
