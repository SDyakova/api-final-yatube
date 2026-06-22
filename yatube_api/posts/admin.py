from django.contrib import admin

from .models import Comment, Follow, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "author", "pub_date", "group")
    list_display_links = ("id", "text")
    search_fields = ("text", "author__username")
    list_filter = ("pub_date", "group")


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug")
    list_display_links = ("id", "title")
    search_fields = ("title",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "post", "text", "created")
    list_display_links = ("id", "text")
    search_fields = ("text", "author__username")


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "following")
    list_display_links = ("id", "user")
    search_fields = ("user__username", "following__username")
