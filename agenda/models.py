from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=255)

class Event(models.Model):
  name = models.CharField(max_length=255)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  local = models.CharField(max_length=255, blank=True)
  link = models.CharField(max_length=255, blank=True)
