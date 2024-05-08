from django.db import models

# Create your models here.
class Event:
  def __init__(self, nome, categoria, local=None, link=None):
    self.nome = nome
    self.categoria = categoria
    self.local = local
    self.link = link

aula_python = Event("Aula de Python", "Backend", "Rio de Janeiro")
aula_js = Event("Aula de JavaScript", "Fullstack", link="https://tamarcado.com/")
events = [
  aula_python, aula_js
]