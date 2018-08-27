# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Emp
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

from django.shortcuts import render

# Create your views here.

def create_emp(request):
    if request.method == 'POST':
        p = Emp.objects.create(
            name = request.POST['name'],
            department = request.POST['department'],
            designation = request.POST['designation'],
        )
        p.save()
        return HttpResponseRedirect('/employeetable/')
    return render(request,'insert.html')

def emp_table(request):
    emp = Emp.objects.all()

    return render(request,'operation.html',locals())

def update_emp(request,id):
    emp = Emp.objects.get(id = id)
    if request.method == 'POST':
        p = Emp.objects.filter(id = emp.id).update(
            name = request.POST['name'],
            department = request.POST['department'],
            designation = request.POST['designation'],
            )
        return HttpResponseRedirect('/employeetable/')

    return render(request,'update.html',locals())

def delete(request,id):
    emp = Emp.objects.get(id = id)
    emp.delete()

    return redirect(request.META['HTTP_REFERER'])
