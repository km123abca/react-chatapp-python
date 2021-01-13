from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class chat(models.Model):
    from_whom = models.CharField(max_length=250)
    msg_content = models.CharField(max_length=1000)
    sent_when = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    parent = models.ForeignKey(
        'self', related_name='replies', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.parent:
            return "{x} says {y} ".format(x=self.from_whom, y=self.msg_content)
        return "{x} says {y} ".format(x=self.from_whom, y=self.msg_content)


class likes(models.Model):
    from_whom = models.CharField(max_length=250)
    parentchat = models.ForeignKey(
        chat, related_name="likeDislikeList", on_delete=models.CASCADE)
    islike = models.BooleanField(default=True)

    def __str__(self):
        return "{x} likes a post from {y}".format(x=self.from_whom, y=self.parentchat.from_whom)
