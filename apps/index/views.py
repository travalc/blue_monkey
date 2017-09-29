# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse

# Create your views here.
def index(request):
    if 'user' in request.session:
        return redirect(reverse('travels:index'))
    return redirect(reverse('log_reg:index'))