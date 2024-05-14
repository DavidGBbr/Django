from datetime import date
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from agenda.models import Event
# Create your views here.
def get_events(request):
    events = Event.objects.filter(date__gte=date.today())
    return render(
       request=request, 
       context={"events": events}, 
       template_name="agenda/list_events.html"
    )


def show_event(request, id):
  event = get_object_or_404(Event,id=id)
  return render(
     request=request, 
     context={"event": event}, 
     template_name="agenda/show_event.html"
  )