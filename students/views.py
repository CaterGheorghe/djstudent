from django.shortcuts import render, redirect
from students.forms import StudentForm
from students.models import Students
from django.http import HttpResponse
from .models import *


def std(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    else:
        form = StudentForm()
    return render(request, 'index.html', {'form': form})


def view(request):
    students = Students.objects.all()
    return render(request, "view.html", {'students': students})


def delete(request, id):
    students = Students.objects.get(id=id)
    students.delete()
    return redirect("/view")


def edit(request, id):
    students = Students.objects.get(id=id)
    return render(request, "edit.html", {'students': students})


def update(request, id):
    students = Students.objects.get(id=id)
    form = StudentForm(request.POST, instance=students)
    if form.is_valid():
        form.save()
        return redirect("/view")
    return render(request, 'edit.html', {'students': students})
