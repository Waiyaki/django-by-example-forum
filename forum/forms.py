from django import forms
from django.contrib.auth.models import User

from .models import Post, Forum, Thread, UserProfile, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('title', 'body')


class ThreadForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = ('title', 'description')


class ForumForm(forms.ModelForm):

    class Meta:
        model = Forum
        fields = ('title', 'description')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('avatar',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
