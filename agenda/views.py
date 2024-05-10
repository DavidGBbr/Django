from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.
def index(request):
  return HttpResponse("Olá mundo!")

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