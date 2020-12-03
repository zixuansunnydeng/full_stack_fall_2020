from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class Tweet(models.Model):
  content = models.TextField()
  user = models.ForeignKey(User, on_delete=CASCADE, related_name='tweets')
  date_posted = models.DateTimeField('date_posted', auto_now=True)

  def __str__(self) -> str:
    return '{} says {}'.format(self.user, self.content)

class Comment(models.Model):
  tweet = models.ForeignKey('Tweet', on_delete=CASCADE, related_name='comments')
  user = models.ForeignKey(User, on_delete=CASCADE)
  content = models.TextField()

  def __str__(self):
    return self.content[:50]


class Follow(models.Model):
  user_from = models.ForeignKey(User, on_delete=CASCADE, related_name='following')
  user_to = models.ForeignKey(User, on_delete=CASCADE, related_name='followers')

  def __str__(self):
    return '{} follows {}'.format(self.user_from, self.user_to)