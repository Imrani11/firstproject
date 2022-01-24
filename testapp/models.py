from django.db import models

# Create your models here.
class login(models.Model):
    firstname = models.CharField(max_length=50)
    email = models.EmailField()