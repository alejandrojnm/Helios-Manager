import time

from django import template
from django.utils.safestring import mark_safe

#TODO : make some imprube
def humanduration(value):
    """
    Filter milisec to human time
    :param value:
    :return:
    """

    time = int(value)
    # days
    if time / 1000 / 3600 > 24:
        days = time / 1000 / 3600 / 24
        return "%i days" % days

    # hours
    if time / 1000 / 60 > 60:
        return "%i hours" % (time / 1000 / 3600)

    # min
    if time / 1000 / 60 < 60:
        return "%i Min" % (time / 1000 / 60)

    # sec
    if time / 1000 < 60:
        return "%i Sec" % (time / 1000)


def systemname(value):
    """
    return the corret img base in de uname of the system
    :param value: str
    :return: str
    """
    if 'Debian' in value:
        return "debian.png"

    if 'Fedora' in value:
        return "fedora.png"

    if 'Ubuntu' in value:
        return "ubuntu.png"

    if 'Centos' in value:
        return "centos.png"

    if 'Redhat' in value:
        return "redhat.png"


def getname(value):
    name = value.split(':')
    return name[0]

def getversion(value):
    name = value.split(':')
    return name[1]

def timestamp(value):
    return time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(value/1000.))


def js(obj):
    """
    Cleaner js from DB for Filter CamanJS
    :param obj:
    :return:
    """
    return mark_safe(obj)


register = template.Library()
register.filter('humanDuration', humanduration)
register.filter('systemName', systemname)
register.filter('getName', getname)
register.filter('getVersion', getversion)
register.filter('timeStamp', timestamp)
register.filter('js', js)
