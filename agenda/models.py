from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return f'{self.name} <{self.id}>'

class Event(models.Model):
  name = models.CharField(max_length=255)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  local = models.CharField(max_length=255, blank=True)
  link = models.CharField(max_length=255, blank=True)
  date = models.DateField(null=True)

  def __str__(self):
      return f'{self.name} <{self.id}>'