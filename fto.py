#!/usr/bin/env python

def rounded(amount, unit = 1):
    t = amount + unit /2
    return t - t % unit


def value(tm, percentage, unit = 2.5):
    return rounded(tm / 0.95 * percentage / 100.0, unit)


def block(tm, percentages, unit = 2.5):
    return map(lambda p: value(tm, p, unit), percentages)


def print_block(exercise, tm, name, percentages, reps, unit = 2.5):
    out = []
    out.append('%-12s %-10s' % (exercise, name))

    weights = block(tm, percentages, unit)
    for i in range(len(weights)):
        out.append('%5.1fkg %-5s' % (weights[i], reps[i]))

    return ' '.join(out)


block_specs = {
    'Warm Up': ((40, 50, 60), ('x 5', 'x 5', 'x 3')),
    'Week 1' : ((65, 75, 85), ('x 5', 'x 5', 'x 5+')),
    'Week 2' : ((70, 80, 90), ('x 3', 'x 3', 'x 3+')),
    'Week 3' : ((75, 85, 95), ('x 5', 'x 3', 'x 1+')),
    'Week 4' : ((40, 50, 60), ('x 5', 'x 5', 'x 5'))
}


if __name__ == '__main__':
    import sys

    tms = map(float, sys.argv[1:])
    exercises = ('OHP', 'Deadlift', 'Bench', 'Squat')

    print 'TMs:',
    for i in range(len(exercises)):
        print exercises[i], '%.1fkg' % tms[i],
    print
    print

    for week in range(1, 5):
        print 'Week %d' % week
        print
        for i in range(len(exercises)):
            for ex, name in ((exercises[i], 'Warm Up'), ('', 'Week %d' % week)):
                specs = block_specs[name]
                print print_block(ex, tms[i], name, specs[0], specs[1], 2.5)
            print
        print

