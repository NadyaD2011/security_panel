from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import get_list_or_404, get_object_or_404
from django.utils.timezone import localtime
from django.shortcuts import render
from datacenter.general_functions import format_duration, get_duration, is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = get_list_or_404(Visit, passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        this_passcard_visits.append(
            {
                'entered_at': localtime(visit.entered_at),
                'duration': format_duration(get_duration(visit)),
                'is_strange': is_visit_long(visit),
            },
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits,
    }
    return render(request, 'passcard_info.html', context)
