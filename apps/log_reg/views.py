# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import *
from .forms import *

#helper function for form errors
def display_form_error(data, request):
    for field in data.errors:
        for message in data.errors[field]:
            string = field + ' field: ' + message
            messages.error(request, string)

# Create your views here.
def index(request):
    #if user is logged in, redirect to home page
    if 'user' in request.session:
        return redirect(reverse('log_reg:success'))
    registration_form = Registration_Form()
    login_form = Login_Form()
    return render(request, 'log_reg/log_reg.html', {'registration_form': registration_form, 'login_form': login_form})

def register(request):
    if request.POST:
        form = Registration_Form(request.POST)
        if form.is_valid():
            data = User.objects.validate_registration(form.cleaned_data, request)
            if data == "Errors found":
                return redirect(reverse('log_reg:index'))
            else:
                request.session['user'] = data
                return redirect(reverse('log_reg:success'))
        else:
            display_form_error(form, request)
            return redirect(reverse('log_reg:log_reg'))
    else:
        messages.error(request, 'invalid request')
        return redirect(reverse('log_reg:index'))

def login(request):
    if request.POST:
        form = Login_Form(request.POST)
        if form.is_valid():
            user = User.objects.validate_login(form.cleaned_data, request)
            if user == 'Errors found':
                return redirect(reverse('log_reg:index'))
            else:
                request.session['user'] = user
                return redirect(reverse('log_reg:success'))
        else:
            display_form_error(form, request)
            return redirect(reverse('log_reg:index'))
    else:
        messages.error(request, 'invalid request')
        return redirect(reverse('log_reg:index'))

def logout(request):
    #clear session and redirect to index when logout is clicked
    request.session.clear()
    return redirect(reverse('log_reg:index'))
#temporary
def success(request):
    #if no user logged in, redirect to login/registration
    if 'user' not in request.session:
        return redirect(reverse('log_reg:index'))
    return render(request, 'log_reg/success.html')