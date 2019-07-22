from django.conf.urls import url
from .views import(
		RetweetView,
		TweetCreateView,
	 	TweetListView, 
	 	TweetDetailView,
	  	TweetUpdateView,
	   	TweetDeleteView
	   	)
from django.views.generic.base import RedirectView
app_name = 'tweets'

urlpatterns = [
	url(r'^$', RedirectView.as_view(url="/")),
	url(r'^create$', TweetCreateView.as_view(), name='create'),
	url(r'^search/$', TweetListView.as_view(), name='list'),
	url(r'^list$', TweetListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/retweet/$', RetweetView.as_view(), name='retweet'),
    url(r'^(?P<pk>\d+)/update$', TweetUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete$', TweetDeleteView.as_view(), name='delete'),
]
    # url(r'^$', tweet_list_view, name='list'),
    # url(r'^(?P<pk>\d+)/$', tweet_detail_view, name='detail'),
    
