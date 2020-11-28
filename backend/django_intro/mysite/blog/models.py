from django.db import models

class Post(models.Model):
  title = models.TextField()
  subtitle = models.TextField()
  author = models.TextField()
  content = models.TextField()
  date_posted = models.DateTimeField('date_posted', auto_now_add=True)
