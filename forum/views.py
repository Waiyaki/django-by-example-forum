from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage


from .models import Forum, Thread, Post
# Create your views here.


def index(request):
    forums = Forum.objects.all()
    forums = make_paginator(request, forums, 20)

    context_dict = {'forums': forums}
    return render(request, 'forum/index.html', context_dict)


def forum(request, pk):
    """
    Listing all threads in a forum with pk=pk.
    """
    forum = Forum.objects.get(pk=pk)
    threads = Thread.objects.filter(forum=pk).order_by('-created')
    threads = make_paginator(request, threads, 20)
    context_dict = {'threads': threads, 'forum': forum}
    return render(request, 'forum/forum.html', context_dict)


def thread(request, pk):
    return HttpResponse('<h1>Work in progress...</h1><a href="/forum/">home</a>')


def make_paginator(request, items, number):
    '''
    Make a paginator of number items of type 'item'
    '''
    paginator = Paginator(items, number)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        items = paginator.page(page)
    except(InvalidPage, EmptyPage):
        items = paginator.page(paginator.num_pages)

    return items


def add_thread(request, pk):
    pass
