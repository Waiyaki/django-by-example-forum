from django.contrib import admin

from .models import Forum, Thread, Post
# Register your models here.


class ForumAdmin(admin.ModelAdmin):
    pass


class ThreadAdmin(admin.ModelAdmin):
    list_display = ['title', 'forum', 'creator', 'created']
    list_filter = ['forum', 'creator']


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'creator']
    list_display = ['title', 'thread', 'creator', 'created']

admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)