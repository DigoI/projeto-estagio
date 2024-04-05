from django.contrib import admin
from post.models import Post, Comment, Like_comment, Like
# Register your models here.

@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display=( 'title','image', 'user')
    list_filter=('user',)
    search_fields=('user', 'title')
@admin.register(Like)
class Likeadmin(admin.ModelAdmin):
    list_display=('post', 'user')
    list_filter=('user', 'post')
    search_fields=('user',)

@admin.register(Comment)
class Commenadmin(admin.ModelAdmin):
    list_display=( 'text', 'post')
    list_filter=('post',)
    search_fields=('post',)