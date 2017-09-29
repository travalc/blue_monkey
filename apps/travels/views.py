# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.
def index(request):
    if 'user' not in request.session:
        return redirect(reverse('index:index'))
    return render(request,'travels/index.html')

def add(request):
    if 'user' not in request.session:
        return redirect(reverse('index:index'))
    add_form = Add_Form()
    return render(request, 'travels/add.html', {'add_form': add_form})

def add_trip(request):
    if request.POST:
        add_form_completed = Add_Form(request.POST)
        if add_form_completed.is_valid():
            data = Trip.objects.validate_add_form(add_form_completed.cleaned_data, request)
            if data == 'Success':
                return redirect(reverse('travels:index'))
            else:
                return redirect(reverse('travels:add'))
        else:
            messages.error('Errors found!')
    else:
        messages.error('invalid request')
        return redirect(reverse('travels:add'))