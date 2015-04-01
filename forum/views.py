from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.decorators import login_required


from .models import Forum, Thread, Post
from .forms import PostForm, ThreadForm, ForumForm, UserForm, UserProfileForm
# Create your views here.


def index(request):
    forums = Forum.objects.order_by('-created')
    forums = make_paginator(request, forums, 20)

    context_dict = {'forums': forums}
    return render(request, 'forum/index.html', context_dict)


def forum(request, pk):
    """
    Listing all threads in a forum with pk=pk.
    """
    forum = get_object_or_404(Forum, pk=pk)
    threads = Thread.objects.filter(forum=pk).order_by('-created')
    threads = make_paginator(request, threads, 20)
    context_dict = {'threads': threads, 'forum': forum}
    return render(request, 'forum/forum.html', context_dict)


def thread(request, pk):
    """
    List posts in this thread.
    """
    # get_object_or_404 ?? get_list_or_404?? Or just no error handling at all here???
    try:
        posts = Post.objects.filter(thread=pk).order_by('created')
    except:
        raise Http404

    posts = make_paginator(request, posts, 15)
    thread = get_object_or_404(Thread, pk=pk)
    context_dict = {'posts': posts, 'thread': thread}
    return render(request, 'forum/thread.html', context_dict)


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


@login_required
def add_thread(request, pk):
    forum = get_object_or_404(Forum, pk=pk)
    if request.method == 'POST':
        thread = Thread(forum=forum)
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.creator = request.user
            thread.save()
            return redirect('forum:forum', pk=pk)
        else:
            print(form.errors)
    else:
        form = ThreadForm()
        context_dict = {'form': form, 'forum': forum}
    return render(request, 'forum/add_thread.html', context_dict)


@login_required
def add_post(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    if request.method == 'POST':
        post = Post(thread=thread)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.creator = request.user
            post.save()
            return redirect('forum:thread', pk=pk)
        else:
            print(form.errors)
    else:
        form = PostForm()
        context_dict = {'form': form, 'thread': thread}
    return render(request, 'forum/add_post.html', context_dict)


@login_required
def create_forum(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.creator = request.user
            forum.save()
            return redirect('forum:index')
        else:
            print(form.errors)
    else:
        form = ForumForm()
    return render(request, 'forum/create_forum.html', {'form': form})


@login_required
def edit_profile(request):
    return HttpResponse("<h1>Work in progress...</h1>")
