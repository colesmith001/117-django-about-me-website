from django.db import models

# Create your models here.
class Skill(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name


class Projects(models.Model):
  name = models.CharField(max_length=50)
  desc = models.TextField()
  year = models.IntegerField()
  img = models.ImageField(upload_to='projectsimg/')
  repository = models.URLField()
  skills = models.ManyToManyField('Skill')

  def __str__(self):
    return self.name