from django.db import models
from django.urls import reverse


# Create your models here.
class Item(models.Model):

    text = models.TextField(default='')
    list = models.ForeignKey(to='List', default=None)


class List(models.Model):

    text = models.TextField(default='')

    def get_absolute_url(self):

        return reverse('view_list', args=(self.id,))
