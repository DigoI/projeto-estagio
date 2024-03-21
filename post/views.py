from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def post(request):
    tf = {
        'Estagio': "de Rodrigo", "18 anos" : 'de idade'
    }
    return HttpResponse(json.dumps(tf))
    