from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    githuburl = models.CharField(max_length=100)

    def __str__(self):
        return self.summary
