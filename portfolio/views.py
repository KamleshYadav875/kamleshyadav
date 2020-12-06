from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Projects, Certificates
import json
# Create your views here.
def indexPage(request):
    projects = Projects.objects.all()
    certificates = Certificates.objects.all()
    return render(request, 'indexPage.html',{"projects":projects,"certificates":certificates})

