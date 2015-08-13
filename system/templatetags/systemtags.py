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

    # sec
    if time / 1000 < 60:
        return "%i Sec" % (time / 1000)

    # min
    if time / 1000 / 60 < 60:
        return "%i Min" % (time / 1000 / 60)

    # hours
    if time / 1000 / 60 > 60:
        return "%i hours" % (time / 1000 / 3600)


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
