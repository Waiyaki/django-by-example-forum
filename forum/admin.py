from django.contrib import admin

from .models import Forum, Thread, Post, UserProfile, Comment
# Register your models here.


class ForumAdmin(admin.ModelAdmin):
    pass


class ThreadAdmin(admin.ModelAdmin):
    list_display = ['title', 'forum', 'creator', 'created']
    list_filter = ['forum', 'creator']


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'creator']
    list_display = ['title', 'thread', 'creator', 'created']


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['title', 'creator']
    list_display = ['title', 'creator']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['avatar', 'posts']

admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Comment, CommentAdmin)
