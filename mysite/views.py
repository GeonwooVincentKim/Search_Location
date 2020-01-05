import datetime

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hi")


# def hi(request):
#     now = datetime.datetime.now()
#     return render(request, 'attribute.html',
#                   {'current_time': now})
