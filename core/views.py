from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse, Http404, HttpResponse
from datetime import datetime
from core.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
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
 
def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        print(request.POST)
        user = authenticate(username=request.POST.get('username',None),password=request.POST.get('password',None))
        print(user)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid Email and Password')

    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

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
            f = form.save(commit=False)
            f.user_type = 'organisation'
            f.save()
            form.save_m2m()
            return redirect('login')
    return render(request,'org_reg.html',{'form': form})
def user_registration(request):
    form = NormalUserForm()
    if request.method == "POST":
        form = NormalUserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user_type = 'normal'
            f.save()
            form.save_m2m()

            return redirect('login')
    return render(request,'user_reg.html',{'form': form})


def create_job(request):
    if not request.user.is_authenticated or not request.user.is_organisation:
        return HttpResponse(status=400)
    form = JobForm()
    if request.method=="POST":
        form = JobForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.company=request.user
            f.save()
            form.save_m2m()
            
            # return redirect('manage-jobs')
    return render(request,'job-create.html',{'form':form})
def resume(request,id):
    user_obj = get_user_model().objects.get(id=id)
    works = Work.objects.filter(user=user_obj)
    educations = Education.objects.filter(user=user_obj)
    return render(request,'resume.html', {'user':user_obj,'works':works,'educations':educations})
    try:
        user_obj = get_user_model().objects.get(id=id)
        works = Work.objects.filter(user=user_obj)
        educations = Education.objects.filter(user=user_obj)
        return render(request,'resume.html', {'user':user_obj,'works':works,'educations':educations})
    except Exception as e:
        print(e)
        return HttpResponse(status=400)
    
def apply_to_job(request):
    pass
def profile(request):
    return render(request,'profile.html')

def view_job(request,id):
    try:
        obj = Job.objects.get(id=id)

        return render(request,'viewjob.html',{'job':obj})
    except:
        return Http404
