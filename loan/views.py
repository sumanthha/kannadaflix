
from django.conf import settings
from django.http import HttpResponse
from django.utils.importlib import import_module
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate
from django.contrib.auth import login as dlogin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def apply_loan(request):
    return render_to_response('loan/apply_loans.html')

def list_loans(request):
    return render_to_response('loan/list_loans.html')
