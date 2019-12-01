from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
  def __init__(self, name, last_name):
    self.name=name
    self.last_name=last_name

def saludo(request):
  doc_externo=open('/var/www/html/proyectos-django/learnDjango/learnDjango/templates/home.html')
  plt=Template(doc_externo.read())
  doc_externo.close()
  ctx=Context()
  document=plt.render(ctx)
  return HttpResponse(document)

def template(request):
  view=get_template('home.html')
  document=view.render({})
  return HttpResponse(document)

def shortcuts(request):
  return render(request, 'extend.html', {'name_person': 'Laura'})

def variables(request):
  p1=Persona('Lalo', 'Díaz')
  temas=['Templates', 'Models']
  otros_temas=[]
  # name='Juanito'
  # last_name='Ramirez'
  doc_externo=open('/var/www/html/proyectos-django/learnDjango/learnDjango/templates/home.html')
  plt=Template(doc_externo.read())
  doc_externo.close()
  ctx=Context({
    'name_person': p1.name, 
    'last_name': p1.last_name,
    'temas': temas,
    'otros_temas': otros_temas
  })
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