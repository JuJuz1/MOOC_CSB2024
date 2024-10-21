from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .utils import access_database

# Views

def homePageView(request):
    return render(request, 'pages/home.html')

def injectionPageView(request):
    results = access_database(request)
    return render(request, 'pages/injection.html', {'results': results})

@login_required
def adminPageView(request):
    # FLAW: Broken access control
    return render(request, 'pages/admin_only.html')
    # FIX:
    # Checking if the user is an admin (is_staff)
    #if not request.user.is_staff:
        #return HttpResponseForbidden("You are not an admin!")
    #return render(request, 'pages/admin_access.html')