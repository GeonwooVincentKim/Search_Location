import datetime

from django.utils import timezone
from .forms import PostForm
from map.models import *
from django.shortcuts import get_object_or_404, render, render_to_response, redirect


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
                    'current_time': now,
                  })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # post = post.filter(published_date__lte=timezone.now())
    # post = post.order_by('created_at')
    # post = Post.objects.all()
    # context = {
    #     'post': post
    # }
    # return render(request, 'post_detail.html', context)
    return render(request, 'post_detail.html',
                  {
                    'post': post
                  })


def save_lnglat(pk, newlnglat):
    post = get_object_or_404(Post, pk=pk)
    post.lnglat = newlnglat
    post.save(['id'])
    return render(pk, 'post_detail.html',
                  {
                      'post': post
                  })
