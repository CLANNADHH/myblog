from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class ArticleView(View):
    def get(self, request):
        return HttpResponse("result")

    def post(self, request):
        return HttpResponse("POST方法")