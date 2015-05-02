from django.conf import settings
from django.http import HttpResponse
from django.utils.importlib import import_module
from django.shortcuts import render_to_response
#import gdata.docs.service
players_details = [ ('a',32,'Right Hand Bat' ),  ]
def index(request):
    if request.user is not None and request.user.is_active == True:
        return render_to_response('home.html', {'loggedin' : True , 'username' : request.user.first_name } )
    return render_to_response('home.html' )


