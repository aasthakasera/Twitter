from django.conf.urls import url

from django.views.generic.base import RedirectView

from tweets.api.views import (
    TweetListAPIView,
    )
app_name="profiles-api"

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/tweets/$', TweetListAPIView.as_view(), name='list'), # /api/tweet/
]