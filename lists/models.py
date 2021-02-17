from django.db import models


# Create your models here.
class Item(models.Model):

    text = models.TextField(default='')
    list = models.ForeignKey(to='List', default=None)


class List(models.Model):

    text = models.TextField(default='')
