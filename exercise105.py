def grades(*args, situation=False):
    infos = dict()
    higher = smaller = sum = 0
    infos['total'] = len(args)

    for note in args:
        if note == 0:
            higher = note
        if note > higher:
            higher = note
    infos['higher'] = higher

    for note in args:
        smaller = note
        if note < smaller:
            smaller = note
    infos['smaller'] = smaller

    for note in args:
        sum += note
    infos['avegare'] = sum/infos['total']

    if situation:
        if infos['average'] < 6:
            infos['situation'] = "BAD"
        elif infos['average'] <= 7:
            infos['situation'] = "GOOD"
        elif infos['average'] >= 9:
            infos['situation'] = "EXCELLENT"
    else:
        pass
    return infos


resp = grades(5.5, 2.5, 1.5, situation=True)
print(resp)
