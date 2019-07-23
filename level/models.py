from django.db import models

# Create your models here.


class Level(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    level_code = models.CharField(max_length=11, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['created']
