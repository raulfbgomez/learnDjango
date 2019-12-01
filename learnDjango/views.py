from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):
  doc_externo=open('/var/www/html/proyectos-django/learnDjango/learnDjango/templates/home.html')
  plt=Template(doc_externo.read())
  doc_externo.close()
  ctx=Context()
  document=plt.render(ctx)
  return HttpResponse(document)

def date(request):
  current_date=datetime.datetime.now()
  return HttpResponse(current_date)

def calculaEdad(request, old, year):
  edadActual=old
  periodo=year-2019
  edadFutura=edadActual + periodo
  documento="<html><h2>En el año %s tendrás %s años</h2></html>" % (year, edadFutura)
  return HttpResponse(documento)