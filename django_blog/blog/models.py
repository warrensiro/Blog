from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto_now_add=True maintains the initial time the object was created
    date_posted = models.DateTimeField(default=timezone.now)
    # if user is deleted, we wanna delete their posts as well
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    # reverse is different from redirect in that redirect returns you to a
    # specific route while reverse returns the full url to that route as a
    # string
    # This is meant to redirect us to the post detail page
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
