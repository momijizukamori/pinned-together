from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Costume, ReferencePhoto, CostumePhoto, Component
from django.contrib.auth.models import User


def index(request):
    template = loader.get_template('costumes/index.html')
    context = { 
        'costume_list' : Costume.objects.all()
    }
    return HttpResponse(template.render(context, request))

def costumepage(request, costume_id):
    template = loader.get_template('costumes/costumepage.html')
    currentcostume = Costume.objects.get(id=costume_id)
    context = { 
        'costume' : currentcostume,
        'refphotos' : ReferencePhoto.objects.filter(costume=costume_id),
        'cosphotos' : CostumePhoto.objects.filter(costume=costume_id),
        'components' : Component.objects.filter(costume=costume_id),
        'cosplayer' : currentcostume.cosplayer,

    }
    return HttpResponse(template.render(context,request))

