from django.db import models
from django.urls import reverse


class List(models.Model):

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

# Create your models here.
class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default='', on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')


    def __str__(self):
        return self.text