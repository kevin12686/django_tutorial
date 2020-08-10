from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(unique=True, max_length=50, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    editTime = models.DateTimeField(auto_now=True, verbose_name='Edit Time')
