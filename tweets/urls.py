from django.conf.urls import url
from tweets.views import Index, Profile, PostTweet


urlpatterns = [
    url(r'^$', Index.as_view()),
    url(r'^user/(\w+)/$', Profile.as_view()),
    url(r'^user/(\w+)/post/$', PostTweet.as_view())
]