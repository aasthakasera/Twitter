from django.conf.urls import url
from .views import(
		TweetCreateView,
	 	TweetListView, 
	 	TweetDetailView,
	  	TweetUpdateView,
	   	TweetDeleteView
	   	)

urlpatterns = [
	url(r'^create$', TweetCreateView.as_view(), name='create'),
	url(r'^$', TweetListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update$', TweetUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete$', TweetDeleteView.as_view(), name='delete'),
]
    # url(r'^$', tweet_list_view, name='list'),
    # url(r'^(?P<pk>\d+)/$', tweet_detail_view, name='detail'),
    
