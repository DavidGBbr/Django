from datetime import date
from django.http.response import HttpResponse
from django.shortcuts import render
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


def show_event(request):
  event = {
    "name":"Teste",
    "category":"Categoria A",
    "local":"Rio de Janeiro"
  }
  # template = loader.get_template("agenda/show_event.html")
  # rendered_template = template.render(context={"event": event}, request=request)
  # return HttpResponse(rendered_template)
  return render(request=request, context={"event": event}, template_name="agenda/show_event.html")