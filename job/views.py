import requests

from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# Create your views here.
@login_required
@csrf_exempt
def showJob(request):
    jobs_request = requests.get('http://' + settings.HELIOS_HOST_MASTER + '/jobs/' + request.POST['id'] + '/status')
    job_json = jobs_request.json()

    jobsList = []
    for job in job_json['taskStatuses'].keys():
        dicc = {'hostname': job, 'name': job_json['taskStatuses'][job]['job']['id'],
                'containerid': job_json['taskStatuses'][job]['containerId'],
                'goal': job_json['taskStatuses'][job]['goal'], 'state': job_json['taskStatuses'][job]['state'],
                'throttled': job_json['taskStatuses'][job]['throttled']}

        ports_list = []
        for port in job_json['taskStatuses'][job]['ports'].keys():
            dicc_job = {'service': port, 'externalport': job_json['taskStatuses'][job]['ports'][port]['externalPort'],
                        'internalport': job_json['taskStatuses'][job]['ports'][port]['internalPort']}
            ports_list.append(dicc_job)

        dicc.update({'ports': ports_list})

        jobsList.append(dicc)

    data = {
        'jobsList': jobsList,
    }
    return render_to_response('showJob.html', data, RequestContext(request))


@login_required
def detailsJob(request, host):

    host_status = requests.get('http://'+settings.HELIOS_HOST_MASTER+'/hosts/'+host+'/status')
    details_host = host_status.json()

    jobsList = []
    for job in details_host['statuses'].keys():
        dicc = {'hostname': job, 'name': details_host['statuses'][job]['job']['id'],
                'containerid': details_host['statuses'][job]['containerId'],
                'goal': details_host['statuses'][job]['goal'], 'state': details_host['statuses'][job]['state'],
                'throttled': details_host['statuses'][job]['throttled'], 'image': details_host['statuses'][job]['job']['image']}

        ports_list = []
        for port in details_host['statuses'][job]['ports'].keys():
            dicc_job = {'service': port, 'externalport': details_host['statuses'][job]['ports'][port]['externalPort'],
                        'internalport': details_host['statuses'][job]['ports'][port]['internalPort']}
            ports_list.append(dicc_job)

        dicc.update({'ports': ports_list})

        jobsList.append(dicc)

    data = {
        'details_host': details_host,
        'jobsList': jobsList,
    }

    return render_to_response('detailsJob.html', data, RequestContext(request))