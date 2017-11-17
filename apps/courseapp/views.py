from __future__ import unicode_literals
from .models import Course
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect


def index(request):
    context = {
       "courses": Course.objects.all(),
   }
    return render(request, "courseapp/index.html",context)


def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
        return redirect('/')
    
    Course.objects.create(
        name = request.POST['name'],
        desc = request.POST['desc'],
        )

    return redirect("/")


def showremovepage(request,course_id):
    context = {
       "course": Course.objects.get(id=course_id)
   }

    return render(request, "courseapp/delete.html",context)


def delete(request,course_id):
        Course.objects.get(id=course_id).delete()
        return redirect('/')