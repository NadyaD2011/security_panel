from django.db.models.fields import duration_microseconds
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.general_functions import format_duration, get_duration, is_visit_long

def storage_information_view(request):
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at=None)
    
    for visit in visits:
        duration= format_duration(get_duration(visit))
        visit = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at),
            'duration': duration,
            'is_strange':  is_visit_long(visit),
        }
        non_closed_visits.append(visit)  
        
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
