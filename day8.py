from functools import reduce
import re
import math


with open("inputs/day8") as file:
    data = file.read()

instruction, nodelist = data.split("\n\n")
instruction = [0 if line == 'L' else 1 for line in list(instruction)]

nodes = {}
for line in nodelist.split("\n"):
    key, values_str = re.split(r"\s*=\s*", line)
    nodes[key] = tuple(map(str.strip, re.findall(r"\b\w+\b", values_str)))

#Part1
steps = 0
current_node = 'AAA'

while current_node != 'ZZZ':
    current_node = nodes[current_node][instruction[steps % len(instruction)]]
    steps += 1

print(steps)

#Part2
start_nodes = [node for node in nodes if node[2] == 'A']

steps = [0 for _ in range(len(start_nodes))]
for i, current_node in enumerate(start_nodes):
    while current_node[2] != 'Z':
        current_node = nodes[current_node][instruction[steps[i] % len(instruction)]]
        steps[i] += 1


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


print(reduce(lcm, steps))

