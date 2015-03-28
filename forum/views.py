from django.shortcuts import render
from django.http import HttpResponse

from .models import Forum
# Create your views here.


def index(request):
    forums = Forum.objects.all()

    context_dict = {'forums': forums}
    return render(request, 'forum/index.html', context_dict)


def forum(request, pk):
    return HttpResponse('<h1>Work in progress...</h1><hr><a href="/forum/">home</a>')


def thread(request, pk):
    return HttpResponse('<h1>Work in progress...</h1><a href="/forum/">home</a>')
