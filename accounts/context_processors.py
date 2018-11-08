from django.utils import timezone

def mycontext(request):
    return {
        'today': timezone.now(),

    }