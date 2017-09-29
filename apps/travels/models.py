# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import datetime
from ..log_reg.models import User
# Create your models here.
#ModelManager for validations
class TripManager(models.Manager):
        #Raise form validation errors if date fields are entered incorrectly
    def validate_add_form(self, data, request):
        errors = []
        travel_from = data['travel_from']
        travel_to = data['travel_to']
        destination = data['destination']
        description = data['description']
        if travel_from < datetime.date.today() or travel_to < datetime.date.today():
            errors.append('Dates entered cannot be in the past.')
        if travel_to < travel_from:
            errors.append('Travel Date To cannot be before Travel Date From')
        if len(destination) < 1:
            errors.append('Destination cannot be blank.')
        if len(description) < 1:
            errors.append('Description cannot be blank.')
        if len(errors) > 0:
            for error in errors:
                messages.error(request, error)
                return 'Errors found'
        user = User.objects.get(username=request.session['user']['username'])
        Trip.objects.create(destination=destination, description=description, 
                            travel_from=travel_from, travel_to=travel_to, created_by=user)
        return 'Success'

class Trip(models.Model):
    destination = models.CharField(max_length=100)
    description = models.TextField()
    travel_from = models.DateField(auto_now_add=False, auto_now=False)
    travel_to = models.DateField(auto_now_add=False, auto_now=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='planned_trips')
    joined_by = models.ManyToManyField(User)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = TripManager()