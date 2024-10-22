from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .utils import getUsersWithClients, getClientOfUser, hash_md5, getHashes

# Views

def homePageView(request):
    return render(request, 'pages/home.html')

@login_required
def searchPageView(request):
    users = getUsersWithClients()
    results = getClientOfUser(request)
    return render(request, 'pages/search.html', {'users': users, 'results': results})

@login_required
def adminPageView(request):
    hashes = getHashes()
    # FLAW: Broken access control
    return render(request, 'pages/admin_only.html', {'hashes': hashes})
    # FIX:
    # Checking if the user is an admin (is_staff)
    #if not request.user.is_staff:
        #return HttpResponseForbidden("You are not an admin!")
    #return render(request, 'pages/admin_access.html')

@login_required
def secureDataPageView(request):
    result = hash_md5(request)
    return render(request, 'pages/secure_data.html', {'result': result})