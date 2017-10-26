from django.contrib import admin
from tweets.models import Tweets, User
# Register your models here.

admin.site.register(User)
admin.site.register(Tweets)
