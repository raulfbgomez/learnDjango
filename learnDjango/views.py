from django.http import HttpResponse
import datetime

def saludo(request):
  return HttpResponse('Hello World')

def date(request):
  current_date=datetime.datetime.now()
  return HttpResponse(current_date)

def calculaEdad(request, old, year):
  edadActual=old
  periodo=year-2019
  edadFutura=edadActual + periodo
  documento="<html><h2>En el año %s tendrás %s años</h2></html>" % (year, edadFutura)
  return HttpResponse(documento)