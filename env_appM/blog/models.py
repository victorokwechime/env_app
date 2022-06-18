from django.db import models

from django.db import models

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField(max_length= "")
    Author = models.CharField(max_length=20)
    Created_date = models.DateField()
    Published_date = models.DateTimeField()
