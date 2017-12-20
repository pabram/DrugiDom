from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Document
from typing import List, Dict

# Create your views here.

def index(request):
    return JsonResponse({
        'success': True,
        'message': 'Hi, this is API.'
    })

def documents(request):
    data = serializers.serialize('json', Document.objects.all())
    # data1 = json.dumps(Document.objects.all())
    
    return JsonResponse({
        'success': True,
        'data': data
    })


