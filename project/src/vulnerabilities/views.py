from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden
from .utils import getUsersWithClients, getClientOfUser, hash_md5, getHashes, createMessage, getMessages

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
    #return render(request, 'pages/admin_only.html', {'hashes': hashes})

@login_required
def secureDataPageView(request):
    result = hash_md5(request)
    return render(request, 'pages/secure_data.html', {'result': result})

@login_required
def messagesPageView(request):
    # FLAW: Insecure design part 1
    message = request.GET.get('message')
    # Not checking if it's empty
    if message != None:
        createMessage(message)
    messages = getMessages()
    return render(request, 'pages/messages.html', {'messages': messages})