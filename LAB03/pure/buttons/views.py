from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('buttons/index.html')
    return HttpResponse(template.render({},request))

def interval(request):
    template = loader.get_template('buttons/interval/index.html')
    return HttpResponse(template.render({},request))

def button(request):
    template = loader.get_template('buttons/button/index.html')
    return HttpResponse(template.render({},request))

def newButton(request):
    template = loader.get_template('buttons/newButton/index.html')
    return HttpResponse(template.render({},request))
# Create your views here.
