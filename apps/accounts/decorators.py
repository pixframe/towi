# STDLIB IMPORTS 
from functools import wraps

# DJANGO CORE IMPORTS
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AnonymousUser


def is_login(view_func):
    @wraps(view_func)
    def new_view_func(request, *args, **kwargs):
        if request.request.user.id is not None:
            return HttpResponseRedirect('/home')
        else:
            return view_func(request, *args, **kwargs)
    return new_view_func


def login_required(view_func):
    @wraps(view_func)
    def new_view_func(request, *args, **kwargs):
        if request.request.user.id is not None:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/inicio')
    return new_view_func
