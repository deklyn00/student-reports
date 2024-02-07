from django.db import models

# Create your models here.
class Item(models.Model):
    userid = models.CharField(null=False, blank=False, max_length=8)
    name = models.CharField(null=False, blank=False, max_length=20)
    surname = models.CharField(null=False, blank=False, max_length=20)
    teacher = models.BooleanField(default=False)
    Mathematics = models.IntegerField(null=False)
    English = models.IntegerField(null=False)
    Physics = models.IntegerField(null=False)
    Biology = models.IntegerField(null=False)
    History = models.IntegerField(null=False)
    Geography = models.IntegerField(null=False)
    Business = models.IntegerField(null=False)


