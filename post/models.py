from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def __str__(self):
        return self.image

class Comment(models.Model):
    text=models.TextField(max_length=500)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text 

class Like(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Like_comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE)
