# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import re
import bcrypt

# ModelManager
class UserManager(models.Manager):
    #Validate registration form fields
    def validate_registration(self, data, request):
        errors = []
        username_regex = re.compile(r'^[A-Za-z0-9]+$')
        name_regex = re.compile(r'^[A-Za-z\s]+$')
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        ***REMOVED*** = User.objects.filter(email=data['email'])
        if len(data['username']) < 3 or len(data['name']) < 3:
            errors.append('Username and name must both be at least 3 characters')
        if not username_regex.match(data['username']):
            errors.append('Username must be letters and numbers only with no spaces.')
        if not name_regex.match(data['name']):
            errors.append('Name must letters and spaces only!')
        if not email_regex.match(data['email']):
            errors.append('Email is improperly formatted')
        if len(***REMOVED***) > 0:
            errors.append('A user with that email already exist')
        if len(data['password']) < 8:
            errors.append('Password must be at least 8 characters')
        if data['password'] != data['confirm_password']:
            errors.append('Password and password confirmation must match')
        if len(errors) > 0:
            for error in errors:
                messages.error(request, error)
                return 'Errors found'
        else:
            username = data['username']
            name = data['name']
            email = data['email']
            password = data['password']
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            birthday = data['birthday']
            self.create(username=username, name=name, email=email, password=hashed_password, birthday=birthday)
            user = {
                'username': username,
                'email': email,
                'name': name,
            }
            return user
    #Validate login info
    def validate_login(self, data, request):
        users = User.objects.filter(username = data['username'])
        if len(users) < 1:
            messages.error(request, 'No user with that username found')
            return 'Errors found'
        else:
            password = data['password']
            #check if password entered matches password in database
            if bcrypt.checkpw(password.encode(), users[0].password.encode()):
                user = {
                    'username': users[0].username,
                    'name': users[0].name,
                    'email': users[0].email,
                    'id': users[0].id
                }
                return user
            else:
                messages.error(request, 'That password does not match what is on file')
                return 'Errors found'

#Model
class User(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = UserManager()