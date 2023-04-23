from django.contrib.gis.db import models


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название", unique=True)
    location = models.PointField(verbose_name="Координаты")
