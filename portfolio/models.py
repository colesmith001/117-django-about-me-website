from django.db import models

# Create your models here.
class Languages(models.Model):
  name = models.CharField(max_length=100)
  years = models.IntegerField()

  def __str__(self):
    return self.name



class Projects(models.Model):
  name = models.CharField(max_length=100)
  desc = models.TextField()
  year = models.IntegerField()
  img = models.ImageField(upload_to='portfolioimg/')
  repo = models.URLField()
  skills = models.ManyToManyField('Languages')

  def __str__(self):
    return self.name