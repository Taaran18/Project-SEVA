"""seva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('register',registration),
    path("about", about, name='about'),
    path("services", services, name='services'),
    path("contact", contact, name='contact'), 
    path('login',login_user,name="login"),
    path('logout',logout_user),
    path('create-job',create_job),
    path('register/user', user_registration),
    path('register/organisation',organisation_registration),
    path('resume/<int:id>',resume),
    path('profile',profile),
    path('job/<int:id>',view_job),
    path('jobs',alljobs),
    path('apply/<int:id>/',job_apply),
    path('myjobs',myjobs),
    path('applicants/<int:id>/',applicants),
    path('job/accept/<int:id>/<int:jobid>/',accept_applicant),
    path('job/reject/<int:id>/<int:jobid>/',reject_applicant),
    path('create-edu',add_edu),
    path('create-work',add_work),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
