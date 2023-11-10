from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse, Http404, HttpResponse
from datetime import datetime
from core.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from .models import *


def index(request):
    jobs = Job.objects.all()
    context = {"jobs": jobs}
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def login_user(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        print(request.POST)
        user = authenticate(
            username=request.POST.get("username", None),
            password=request.POST.get("password", None),
        )
        print(user)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid Email and Password")

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("home")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(
            name=name, email=email, phone=phone, desc=desc, date=datetime.today()
        )
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request, "contact.html")


def registration(request):
    org_form = OrganizationUserForm()
    user_form = NormalUserForm()
    return render(
        request, "register.html", {"org_form": org_form, "user_form": user_form}
    )


def organisation_registration(request):
    form = OrganizationUserForm()
    if request.method == "POST":
        form = OrganizationUserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user_type = "organisation"
            f.save()
            form.save_m2m()
            return redirect("login")
    return render(request, "org_reg.html", {"form": form})


def user_registration(request):
    form = NormalUserForm()
    if request.method == "POST":
        form = NormalUserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user_type = "normal"
            f.save()
            form.save_m2m()

            return redirect("login")
    return render(request, "user_reg.html", {"form": form})


def create_job(request):
    if not request.user.is_authenticated or not request.user.is_organisation:
        return HttpResponse(status=400)
    form = JobForm()
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.company = request.user
            f.save()
            form.save_m2m()

            return redirect("home")
    return render(request, "job-create.html", {"form": form})


def resume(request, id):
    user_obj = get_user_model().objects.get(id=id)
    works = Work.objects.filter(user=user_obj)
    educations = Education.objects.filter(user=user_obj)
    return render(
        request,
        "resume.html",
        {"user": user_obj, "works": works, "educations": educations},
    )
    try:
        user_obj = get_user_model().objects.get(id=id)
        works = Work.objects.filter(user=user_obj)
        educations = Education.objects.filter(user=user_obj)
        return render(
            request,
            "resume.html",
            {"user": user_obj, "works": works, "educations": educations},
        )
    except Exception as e:
        print(e)
        return HttpResponse(status=400)


@login_required
def job_apply(request, id):
    if request.user.user_type == "normal":
        try:
            job = Job.objects.get(id=id)
            job.applicants.add(request.user)
            job.save()
            obj = AppliedJob.objects.create(user=request.user, job=job)
            obj.save()
            messages.success(request, "Successfully Applied")
            return redirect("home")
        except Exception as e:
            print(e)
            messages.error(request, "Job ID doesn't exists")
            return redirect("home")
    else:
        messages.error(request, "Only Users can apply for jobs")
        return redirect("home")
    return HttpResponse("nothing worked" + request.user.user_type)


def profile(request):
    work = Work.objects.filter(user=request.user)
    edu = Education.objects.filter(user=request.user)
    return render(request, "profile.html", {"work": work, "edu": edu})


def alljobs(request):
    jobs = Job.objects.all()
    return render(request, "jobs.html", {"jobs": jobs})


def view_job(request, id):
    try:
        obj = Job.objects.get(id=id)

        return render(request, "viewjob.html", {"job": obj})
    except:
        return Http404


@login_required
def myjobs(request):
    if request.user.user_type == "normal":
        jobs = AppliedJob.objects.filter(user=request.user)
        return render(request, "myjobs.html", {"jobs": jobs})
    else:
        return redirect("home")


def accept_applicant(request, id, jobid):
    try:
        obj = AppliedJob.objects.get(user__id=id, job__id=jobid)
        if obj.job.company == request.user:
            obj.status = "accepted"
            obj.closed = True
            obj.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse("You are not job poster", status=400)
    except Exception as e:
        print(e)
        return HttpResponse("No Job id exists", status=400)


def reject_applicant(request, id, jobid):
    try:
        obj = AppliedJob.objects.get(user__id=id, job__id=jobid)
        if obj.job.company == request.user:
            obj.status = "rejected"
            obj.closed = True
            obj.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse("You are not job poster", status=400)
    except:
        return HttpResponse("No Job id exists", status=400)


def applicants(request, id):
    job = Job.objects.get(id=id)
    applicants = job.applicants.all()
    applied_jobs = []

    for i in applicants:
        try:
            applied_jobs.append(AppliedJob.objects.get(job__id=id, user=i))
        except Exception as e:
            print(e)
            continue

    return render(
        request,
        "applicants.html",
        {
            "applicants": applicants,
            "job_id": id,
            "zipdata": zip(applicants, applied_jobs),
        },
    )


@csrf_exempt
def add_work(request):
    data = request.POST
    w = Work.objects.create(
        user=request.user,
        title=data["title"],
        institute=data["institute"],
        desc=data["desc"],
        from_year=data["from_year"],
        to_year=data["to_year"],
    )
    w.save()
    return HttpResponse(status=200)


@csrf_exempt
def add_edu(request):
    data = request.POST
    w = Education.objects.create(
        user=request.user,
        title=data["title"],
        institute=data["institute"],
        from_year=data["from_year"],
        to_year=data["to_year"],
    )
    w.save()
    return HttpResponse(status=200)
