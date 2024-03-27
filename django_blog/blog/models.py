from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto_now_add=True maintains the initial time the object was created
    date_posted = models.DateTimeField(default=timezone.now)
    # if user is deleted, we wanna delete their posts as well
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
