from django.utils.timezone import localtime


def get_duration(visit):
    time_entered = localtime(visit.entered_at)
    time_leaved = localtime(visit.leaved_at)
    time = time_leaved - time_entered
    return time.total_seconds()


def format_duration(duration):
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    return f'{hours}:{minutes}'


def is_visit_long(visit):
    hour = 60
    seconds = get_duration(visit)
    time = int(seconds // hour)
    return time >= hour
