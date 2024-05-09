from django.http.response import HttpResponse
from django.shortcuts import render
from agenda.models import events
from django.template import loader
# Create your views here.
def index(request):
  return HttpResponse("Olá mundo!")

def show_event(request):
  event = events[0]
  # template = loader.get_template("agenda/show_event.html")
  # rendered_template = template.render(context={"event": event}, request=request)
  # return HttpResponse(rendered_template)
  return render(request=request, context={"event": event}, template_name="agenda/show_event.html")