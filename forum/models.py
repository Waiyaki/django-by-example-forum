from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class Forum(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, blank=True, null=True)

    def num_posts(self):
        return sum([thread.num_posts() for thread in self.thread_set.all()])

    def num_threads(self):
        return self.thread_set.count()

    def last_post(self):
        if self.thread_set.count():
            last = None
            for thread in self.thread_set.all():
                l = thread.last_post()
                if l:
                    if not last:
                        last = l
                    elif l.created > last.created:
                        last = l
            return last

    def __str__(self):
        return self.title


class Thread(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, blank=True, null=True)
    forum = models.ForeignKey(Forum)

    def __str__(self):
        return str(self.creator) + " - " + self.title

    def num_posts(self):
        return self.post_set.count()

    def num_replies(self):
        return self.post_set.count()

    def last_post(self):
        if self.post_set.count():
            return self.post_set.order_by('-created')[0]


class Post(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, blank=True, null=True)
    thread = models.ForeignKey(Thread)
    body = models.TextField(max_length=10000)

    def __str__(self):
        return "{} - {} - {}".format(self.creator, self.thread, self.title)

    def short(self):
        return "{} - {}".format(self.creator, self.title)
    short.allow_tags = True


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='profile_images', blank=True, null=True)
    posts = models.IntegerField(default=0)
    thumbnail1 = models.ImageField(upload_to='profile_images/thumbs/', blank=True, null=True)
    thumbnail2 = models.ImageField(upload_to='profile_images/thumbs/', blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_thumb_one(self):
        # Have to check if user.userprofile.avatar in template lest avatar be empty and the link reads /media/None
        return str(settings.MEDIA_URL + (self.thumbnail1.name if self.thumbnail1.name else self.avatar.name))

    def get_thumb_two(self):
        return str(settings.MEDIA_URL + (self.thumbnail2.name if self.thumbnail2.name else self.avatar.name))

    def get_avatar(self):
        return str(settings.MEDIA_URL + self.avatar.name)
