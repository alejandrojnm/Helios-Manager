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

def js(obj):
    """
    Cleaner js from DB for Filter CamanJS
    :param obj:
    :return:
    """
    return mark_safe(obj)


register = template.Library()
register.filter('humanDuration', humanduration)
register.filter('js', js)
