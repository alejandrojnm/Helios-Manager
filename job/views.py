import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import requests

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
    host_status = requests.get('http://' + settings.HELIOS_HOST_MASTER + '/hosts/' + host + '/status')
    details_host = host_status.json()

    jobsList = []
    for job in details_host['statuses'].keys():
        dicc = {'hostname': job, 'name': details_host['statuses'][job]['job']['id'],
                'containerid': details_host['statuses'][job]['containerId'],
                'goal': details_host['statuses'][job]['goal'], 'state': details_host['statuses'][job]['state'],
                'throttled': details_host['statuses'][job]['throttled'],
                'image': details_host['statuses'][job]['job']['image']}

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


@login_required
def listAllJob(request):
    jobs_request = requests.get('http://' + settings.HELIOS_HOST_MASTER + '/jobs/')
    job_json = jobs_request.json()

    list_job = []
    for job in job_json.keys():
        dicc = {"id": job, "image": job_json[job]['image'], "creatingUser":job_json[job]['creatingUser']}
        list_job.append(dicc)

    data = {
        'listJob': list_job,
    }

    return render_to_response('listJob.html', data, RequestContext(request))

@login_required
def showAllJob(request):
    if request.is_ajax():
        jobs_request = requests.get('http://' + settings.HELIOS_HOST_MASTER + '/jobs/')
        job_json = jobs_request.json()

        job_list = []
        for job in job_json.keys():
            name = job.split(':')
            list = {'id':job, 'name': name[0]+':'+name[1]}
            job_list.append(list)

        return HttpResponse(json.dumps(job_list), content_type='application/json')

@csrf_exempt
@login_required
def deployJob(request):
    if request.is_ajax():
        body = {"goal": "START", "deployerUser": "root", "jobId": request.POST['job']}
        headers = {'content-type': 'application/json'}
        jobs_deploy = requests.put('http://' + settings.HELIOS_HOST_MASTER + '/hosts/'+ request.POST['host'] +'/jobs/'+ request.POST['job'] +'?token=&user=root', data=json.dumps(body), headers=headers)
        jobs_result = jobs_deploy.json()
        list = {'status':jobs_result['status'], 'job': jobs_result['job']}

        return HttpResponse(json.dumps(list), content_type='application/json')

@csrf_exempt
@login_required
def undeployJob(request):
    if request.is_ajax():
        jobs_delete = requests.delete('http://' + settings.HELIOS_HOST_MASTER + '/hosts/'+request.POST['host']+'/jobs/'+request.POST['job']+'/')
        jobs_result = jobs_delete.json()
        list = {'status':jobs_result['status'], 'job': jobs_result['job']}

        return HttpResponse(json.dumps(list), content_type='application/json')

@csrf_exempt
@login_required
def startstopJob(request):
    if request.is_ajax():
        if request.POST['status'] == 'RUNNING':
            body = {"goal": "STOP", "deployerUser": "null", "jobId": request.POST['job']}

        if request.POST['status'] == 'STOPPED':
            body = {"goal": "START", "deployerUser": "null", "jobId": request.POST['job']}

        headers = {'content-type': 'application/json'}
        jobs_startstop = requests.patch('http://' + settings.HELIOS_HOST_MASTER + '/hosts/'+request.POST['host']+'/jobs/'+request.POST['job']+'/', data=json.dumps(body), headers=headers)
        jobs_result = jobs_startstop.json()

        list = {'status':jobs_result['status'], 'job': jobs_result['job'], 'host': jobs_result['host']}

        return HttpResponse(json.dumps(list), content_type='application/json')