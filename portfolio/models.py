from django.db import models
from rest_framework import serializers

# Create your models here.
class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150,)
    desc = models.CharField(max_length=500)
    githubLink = models.TextField()
    liveLink = models.TextField(blank=True)
    img = models.ImageField(upload_to='projects')

    def __str__(self):
        return self.title


class Certificates(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150,)
    img = models.ImageField(upload_to='languages')

    def __str__(self):
        return self.title
    

