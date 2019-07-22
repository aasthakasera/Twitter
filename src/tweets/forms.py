from django import forms
from django.db import models
from .models import Tweet

class TweetModelForm(forms.ModelForm):
	# title = forms.TextInput()
	title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':"Title",'size': '40'}))
	content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':"Your message",
		"class":"form-control"}))
	class Meta:
		model = Tweet
		fields = [
			# "user",
			"title",
			"content",
		]

	def clean_content(self, *args, **kwargs):
		content = self.cleaned_data.get("content")
		if content == "abc":
			raise forms.ValidationError("Cannot be ABC")
		return content