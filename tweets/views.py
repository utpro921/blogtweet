# from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
# Create your views here.


class Index(View):
    def get(self, request):
        params = dict()
        params["name"] = "Help"
        return render(request, 'base.html', params)

    def post(self, request):
        return HttpResponse("POST")

