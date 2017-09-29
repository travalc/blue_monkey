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
    user = User.objects.get(username=request.session['user']['username'])
    user_trips_query = user.planned_trips.all()
    joined_trips = user.joined_trips.all()
    all_trips = Trip.objects.all().exclude(created_by=user.id).exclude(joined_by=user.id)
    return render(request,'travels/index.html', {'user_trips': user_trips_query, 'all_trips': all_trips, 'joined_trips': joined_trips})

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
            messages.error(request, 'Errors found!')
    else:
        messages.error('invalid request')
        return redirect(reverse('travels:add'))

def join(request):
    if request.POST:
        user = User.objects.get(username=request.session['user']['username'])
        trip = Trip.objects.get(id=request.POST['id'])
        trip.joined_by.add(user)
        return redirect(reverse('travels:index'))
    else:
        messages.error('invalid request')
        return redirect(reverse('travels:index'))

def destination(request, id):
    trip = Trip.objects.get(id=id)
    joined_users = User.objects.filter(joined_trips__id=id)
    return render(request, 'travels/destination.html', {'trip': trip, 'joined_users': joined_users})