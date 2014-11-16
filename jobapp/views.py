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
@csrf_exempt
def showJob(request):

    jobs_request = requests.get('http://'+settings.HELIOS_HOST_MASTER+'/jobs/'+request.POST['id']+'/status')
    job_json = jobs_request.json()

    jobsList = []
    for job in job_json['taskStatuses'].keys():
        dicc = {'hostname': job, 'name': job_json['taskStatuses'][job]['job']['id'], 'containerid': job_json['taskStatuses'][job]['containerId'],'goal': job_json['taskStatuses'][job]['goal'], 'state': job_json['taskStatuses'][job]['state'], 'throttled': job_json['taskStatuses'][job]['throttled']}

        ports_list = []
        for port in job_json['taskStatuses'][job]['ports'].keys():
            dicc_job = {'service': port, 'externalport': job_json['taskStatuses'][job]['ports'][port]['externalPort'], 'internalport': job_json['taskStatuses'][job]['ports'][port]['internalPort']}
            ports_list.append(dicc_job)

        dicc.update({'ports': ports_list})

        jobsList.append(dicc)

    data = {
        'jobsList': jobsList,
    }
    return render_to_response('jobDetails.html', data, RequestContext(request))