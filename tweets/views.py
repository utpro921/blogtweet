# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
from tweets.models import User, Tweets, HashTag
from tweets.forms import TweetForm
# Create your views here.


class Index(View):
    def get(self, request):
        params = dict()
        params["name"] = "Help"
        return render(request, 'base.html', params)

    def post(self, request):
        return HttpResponse("POST")


class Profile(View):
    def get(self, request, username):
        print(username)
        params = dict()
        user = User.objects.get(username=username)
        print(user)
        tweets = Tweets.objects.filter(user=user)
        print(tweets)
        params["user"] = user
        params["tweets"] = tweets
        return render(request, "profile.html", params)


class PostTweet(View):
    def post(self, request, username):
        form = TweetForm(self.request.POST)
        if form.is_valid():
            user = User.objects.get(username=username)
            tweet = Tweets(text=form.cleaned_data['text'],
                           user=user, country=form.cleaned_data['country'])
            tweet.save()
            words = form.cleaned_data['text'].split(" ")
            for word in words:
                if word[0] == "#":
                    hashtag, created = HashTag.objects.get_or_create(name=word[1:])
                    hashtag.tweet.add(tweet)
            return HttpResponseRedirect('/user/'+username)
