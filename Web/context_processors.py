from django.conf import settings


def expose_extra_settings_keys(request):
    return {
        'RESULTS_DAYS': settings.RESULTS_DAYS
    }