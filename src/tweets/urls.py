from django.conf.urls import url
from .views import tweet_detail_view, tweet_list_view

urlpatterns = [
    url(r'^$', tweet_list_view),
    url(r'^1/$', tweet_detail_view),
]
