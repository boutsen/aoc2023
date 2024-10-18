import re
DATA = open("inputs/day19", "r").read().split('\n\n')

#print(DATA[0])

START_WF_NAME = 'in'
ACCEPT = 'A'
REJECT = 'R'

def parse_instruction(instructions):
    i = set()
    regex = re.compile(r'{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}')
    for line in instructions.split('\n'):
        i.add(tuple(map(int, re.search(regex, line).groups())))

    return i


def parse_rules(rules):
    wf = {}
    regex = re.compile(r'([a-zA-Z]+[<>]\d+):([a-zA-Z]+)')
    for rule in rules.split('\n'):
        ci = rule.index('{')
        rest = rule[ci+1:-1]
        d = rest.split(',')[-1]
        r = []
        m = re.findall(regex, rest)
        for M in m:
            r.append((M[0], M[1]))
        r.append(('True', d))
        wf[rule[:ci]] = r

    return wf


def is_accepted(part, wf):
    x, m, a, s = part
    part_dict = {
        'x': x,
        'm': m,
        'a': a,
        's': s
    }

    c = START_WF_NAME
    while c not in [ACCEPT, REJECT]:
        for rule in wf[c]:
            condition, success = rule
            if eval(condition, part_dict):
                c = success
                break

    return c == ACCEPT

parts = parse_instruction(DATA[1])
wf = parse_rules(DATA[0])

s = 0
for part in parts:
    if is_accepted(part, wf) == True:
        s += sum(part)

print(s)