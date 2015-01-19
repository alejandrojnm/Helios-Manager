import json
import requests
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext
from django.db.models import Q
from django.utils.http import urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.conf import settings

# Create your views here.
@login_required
def list_host(request):

    allhost = requests.get('http://'+settings.HELIOS_HOST_MASTER+'/hosts/')
    allh = allhost.json()

    listHost = []
    for host in allh:
        tempo = requests.get('http://'+settings.HELIOS_HOST_MASTER+'/hosts/'+host+'/status')
        listHost.append(tempo.json())

    data = {
        'listHost': listHost,
    }

    return render_to_response('listHost.html', data, RequestContext(request))