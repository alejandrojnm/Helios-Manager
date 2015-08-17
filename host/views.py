import json
from django.http import HttpResponse
import requests
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.conf import settings

# Create your views here.
@login_required
def list_host(request):

    allhost = requests.get('http://'+settings.HELIOS_HOST_MASTER+'/hosts/')
    allh = allhost.json()

    listHost = []
    for host in allh:
        host_list = requests.get('http://'+settings.HELIOS_HOST_MASTER+'/hosts/'+host+'/status')
        listHost.append(host_list.json())

    data = {
        'listHost': listHost,
    }

    return render_to_response('listHost.html', data, RequestContext(request))

@login_required
def details_host(request, host):

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

    return render_to_response('detailsHost.html', data, RequestContext(request))

@login_required
def host_memory(request, host):
    host_status = requests.get('http://'+settings.HELIOS_HOST_MASTER+'/hosts/'+host+'/status')
    details_host = host_status.json()

    msg = {'memory': details_host['hostInfo']['memoryTotalBytes']-details_host['hostInfo']['memoryFreeBytes']}

    return HttpResponse(json.dumps(msg))

@login_required
def host_swap(request, host):
    host_status = requests.get('http://'+settings.HELIOS_HOST_MASTER+'/hosts/'+host+'/status')
    details_host = host_status.json()

    msg = {'swap': details_host['hostInfo']['swapTotalBytes']-details_host['hostInfo']['swapFreeBytes']}

    return HttpResponse(json.dumps(msg))