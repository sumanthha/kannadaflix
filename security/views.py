
from django.conf import settings
from django.http import HttpResponse
from django.utils.importlib import import_module
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate
from django.contrib.auth import login as dlogin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#def login_required(request):
#    if request.user is None or request.user.is_active == False:
#        return render_to_response('security/login.html')
#    return render_to_response('security/success.html', {'loggedin' : True , 'username' : request.user.first_name } )


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        dlogin(request,user)
        return render_to_response('security/success.html', {'user' : user } )
    if request.user is not None and request.user.is_active == True:
        return render_to_response('security/success.html', {'user' : request.user } )
    return render_to_response('security/login.html')

from django.contrib.auth import logout
def signoff(request):
    logout( request )
    return render_to_response('security/login.html')

def join(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        retypepassword = request.POST['retypepassword']
        user = User.objects.create_user(username, email,password)
        user.last_name = lastname
        user.first_name = firstname
        user.save()
        request.user = user
        return render_to_response('security/success.html', {'user' : request.user } )
    return render_to_response('security/join.html')

from security.models import Account
from django.core.exceptions import ObjectDoesNotExist
@login_required
def account_summary(request):
    try:
        account = Account.objects.get( user = request.user )
    except ObjectDoesNotExist:
        account = Account( user = request.user )
        account.save()
        print account
    return render_to_response('security/account_summary.html', {
        'user' : request.user,
        'account' : account,
    })
   
