from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Forum(models.Model):
    title = models.CharField(max_length=60)

    def num_posts(self):
        return sum([thread.num_posts() for thread in self.thread_set.all()])

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
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    forum = models.ForeignKey(Forum)

    def __str__(self):
        return str(self.creator) + " - " + self.title

    def num_posts(self):
        return self.post_set.count()

    def num_replies(self):
        return self.post_set.count() - 1

    def last_post(self):
        if self.post_set.count():
            return self.post_set.order_by('-created')[0]


class Post(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    thread = models.ForeignKey(Thread)
    body = models.TextField(max_length=10000)

    def __str__(self):
        return "{} - {} - {}".format(self.creator, self.thread, self.title)

    def short(self):
        return "{} - {}\n{}".format(self.creator, self.title, self.created.strftime("%b %d, %I:%M %p"))
    short.allow_tags = True
