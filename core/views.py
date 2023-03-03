from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, Http404
from datetime import datetime
from core.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate
from .forms import *
from .models import *
def index(request):
    jobs = Job.objects.all()
    context = {'jobs':jobs}
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')
 
def login(request):
    return render(request,'login.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

def registration(request):
    org_form = OrganizationUserForm()
    user_form = NormalUserForm()
    return render(request,'register.html',{'org_form': org_form,'user_form': user_form})
def organisation_registration(request):
    form = OrganizationUserForm()
    if request.method == "POST":
        form = OrganizationUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpRequest('/login')
    return render(request,'org_reg.html',{'form': form})
def user_registration(request):
    form = NormalUserForm()
    if request.method == "POST":
        form = NormalUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpRequest('/login')
    return render(request,'user_reg.html',{'form': form})

def resume(request):
    return render(request,'resume.html')
def apply_to_job(request):
    pass
def profile(request):
    return render(request,'profile.html')
