from django.conf.urls import url
from tweets.views import Index


urlpatterns = [
    url(r'^', Index.as_view())
]