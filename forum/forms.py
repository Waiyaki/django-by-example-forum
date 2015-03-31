from django import forms

from .models import Post, Forum, Thread


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body')


class ThreadForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = ('title',)


class ForumForm(forms.ModelForm):

    class Meta:
        model = Forum
        fields = ('title',)
