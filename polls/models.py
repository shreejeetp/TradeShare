from django.db import models

class Users(models.Model):
    email = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    password=models.CharField(max_length=128)
    date = models.DateField()

    def __unicode__(self):
        return self.name
# Create your models here.
