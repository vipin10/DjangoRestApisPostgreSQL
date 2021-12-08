from django.db import models


class Tutorial(models.Model):
    que = models.CharField(max_length=70, blank=False, default='')
    opt1 = models.CharField(max_length=200, blank=True, default='')
    opt2 = models.CharField(max_length=200, blank=True, default='')
    opt3 = models.CharField(max_length=200, blank=True, default='')
    opt4 = models.CharField(max_length=200, blank=True, default='')
    que_type = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False)
