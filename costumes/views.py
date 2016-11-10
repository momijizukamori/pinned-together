from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Costume, ReferencePhoto, CostumePhoto, Component


def index(request):
    template = loader.get_template('costumes/index.html')
    context = { 
        'costume_list' : Costume.objects.all()
    }
    return HttpResponse(template.render(context, request))

def costumepage(request, costume_id):
    template = loader.get_template('costumes/costumepage.html')
    context = { 
        'costume' : Costume.objects.get(id=costume_id),
        'refphotos' : ReferencePhoto.objects.filter(costume=costume_id),
        'cosphotos' : CostumePhoto.objects.filter(costume=costume_id),
        'components' : Component.objects.filter(costume=costume_id),
    }
    return HttpResponse(template.render(context,request))

