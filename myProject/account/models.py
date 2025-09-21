from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User, related_name="post_like", blank=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.like.count()    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='avatars/', default='avatars/default.jpg')
    bio = models.TextField(blank=True)
    following = models.ManyToManyField(User, related_name="followers", blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"
