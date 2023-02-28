from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, Http404

def index(request):
    return render(request, 'index.html')
