from django.contrib import admin
from django.contrib.auth.models import User
from post.models import Post, Like_comment, Like, Comment

# Register your models here.

class Useradmin(admin.ModelAdmin):
    list_display=( 'username', 'email','age')
    list_filter= ('username', 'age')
    search_fields=('username', 'email')

