from django.http.response import HttpResponse
from django.shortcuts import render
from agenda.models import events
# Create your views here.
def index(request):
  return HttpResponse("Olá mundo!")

def show_event(request):
  event = events[1]
  return HttpResponse(f""" 
  <html>
    <h1>Evento: {event.nome}</h1>                    
    <p>Evento: {event.categoria}</p>                    
    <p>Evento: {event.local}</p>                    
    <p>Evento: {event.link}</p>                    
  </html>
""")