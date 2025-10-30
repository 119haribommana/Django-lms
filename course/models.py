from django.db import models 

class Course(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    trainer=models.ForignKey
