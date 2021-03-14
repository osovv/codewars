def format_duration(seconds):
    from collections import OrderedDict
    durations = OrderedDict([
        ('year', 31536000),
        ('day', 86400),
        ('hour', 3600),
        ('minute', 60),
        ('second', 1)
      ])
    times = OrderedDict([
        ('year', 0),
        ('day', 0),
        ('hour', 0),
        ('minute', 0),
        ('second', 0)
    ])
    
    for key in times:
        times[key] = int(seconds / durations[key])
        seconds %= durations[key]
    result = []
    for k, v in times.items():
        if v == 0:
            continue
        if v == 1:
            result.append(f'{v} {k}')
        else:
            result.append(f'{v} {k}s')
    if len(result) > 1:
        return '{} and {}'.format(', '.join(result[:-1]), result[-1])
    elif result:
        return result[0]
    else:
        return 'now'

