import json
import requests

from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext
from django.db.models import Q
from django.utils.http import urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from django.conf import settings

# Create your views here.
@login_required
def dashboard(request):
    allhost = requests.get('http://10.10.10.34:5801/hosts/')
    allh = allhost.json()

    alljobs = requests.get('http://10.10.10.34:5801/jobs/')
    allj = alljobs.json()


    listHost = []
    for host in allh:
        tempo = requests.get('http://10.10.10.34:5801/hosts/'+host+'/status')
        listHost.append(tempo.json())

    jobs = []
    for job in allj:
        dicc = {'id': allj[job]['id'], 'name': job.split(':')[0], 'version':job.split(':')[1]}

        ports_list = []
        for port in allj[job]['ports']:
            ports_list.append(allj[job]['ports'][port]['internalPort'])

        dicc.update({'ports': ports_list})

        jobs.append(dicc)

    data = {
        'listHost': listHost,

        'listJobs': jobs,
        'version': settings.HELIOS_VERSION,
    }
    return render_to_response('dashboard.html', data, RequestContext(request))