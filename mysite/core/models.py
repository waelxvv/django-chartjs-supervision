from django.db import models


class Data(models.Model):
    time = models.CharField(max_length=30)
    power = models.IntegerField()
