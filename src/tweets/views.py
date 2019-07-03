from django.shortcuts import render
from .models import Tweet

# Create your views here.
def tweet_detail_view(request, id=1):
	obj = Tweet.objects.get(id=id)
	print(obj)
	context = {
		"object" : obj
	}
	return render(request, "detail.html", {})

def tweet_list_view(request):
	queryset = Tweet.objects.all()
	for i in queryset:
		print(i )
	context = {
		"object_list" : queryset
	}
	return render(request, "list.html", {})