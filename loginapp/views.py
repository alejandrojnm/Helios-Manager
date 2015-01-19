import json
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
def login_helios(request):

    data = {
        'version': settings.HELIOS_MANAGER_VERSION,
    }

    return render_to_response('login.html', data, RequestContext(request))

def loginauth(request):
    """
    System Login using ajax
    :param request:
    :return: true or false
    """
    if request.is_ajax():
        username = request.POST['user']
        password = request.POST['passwd']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                msg = {'status': True, 'url': reverse('dashboard')}
                return HttpResponse(json.dumps(msg))
            else:
                msg = {'status': False, 'msg': 'Disable Account'}
                return HttpResponse(json.dumps(msg))
        else:
            # Return an 'invalid login' error message.
            msg = {'status': False, 'msg': 'User or password not valid'}
            return HttpResponse(json.dumps(msg))
    else:
        return HttpResponse('Invalid Request')