import datetime

from map.models import *
from django.shortcuts import get_object_or_404, render, render_to_response
# from geoposition.fields import GeopositionField


# Create your views here.
def hi(request):
    now = datetime.datetime.now()
    return render(request, 'template.html', {'current_time': now})


# def index(request):
#     now = datetime.datetime.now()
#     return render(request, 'template.html', {'current_time': now})

def index(request):
    post_list = Post.objects.all()
    now = datetime.datetime.now()
    return render(request, 'template.html',
                  {
                    'post_list': post_list,
                    'post_lat': post_detail,
                    'current_time': now,
                  })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html',
                  {
                    'post': post
                  })


def save_lnglat(request, pk, newlnglat):
    post = get_object_or_404(Post, pk=pk)
    post.lnglat = newlnglat
    post.save()
    return render(request, 'post_detail.html',
                  {
                      'post': post
                  })
