from django.db import models

class Post(models.Model):
    article = models.CharField(max_length=200)

