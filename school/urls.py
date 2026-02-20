"""
URL configuration for learner2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('blog-details/',views.blog_details,name='blog_details'),
    path('contact/',views.contact,name='contact'),
    path('courses_details/',views.courses_details,name='courses_details'),
    path('enroll/',views.enroll,name='enroll'),
    path('events/',views.events,name='events'),
    path('index/',views.index,name='index'),
    path('instructors/',views.instructors,name='instructors'),
    path('instructor-profile/',views.instructor_profile,name='instructor_profile'),
    path('pricing/',views.pricing,name='pricing'),
    path('starter_page/',views.starter_page,name='starter_page'),
    path('privacy/',views.privacy,name='privacy'),
    path('terms/',views.terms,name='terms'),
]
