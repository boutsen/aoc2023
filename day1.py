import re

DATA = open("inputs/day1", "r")
DATA2 = open("inputs/day1", "r")

def get_digits(lines):
    return [int(line[0]+line[-1]) if line else 0 for line in [re.sub('\D', '', line) for line in lines]]

def get_digits_and_translate(lines):
    map = {'zero': '0',
           'one': '1',
           'two': '2',
           'three': '3',
           'four': '4',
           'five': '5',
           'six': '6',
           'seven': '7',
           'eight': '8',
           'nine': '9',
           }
    return [int((map[line[0]]
                 if line[0] in map
                 else line[0])+(map[line[-1]]
                                                if line[-1] in map
                                                else line[-1]))
            for line in [re.findall(r'(?=('+'|'.join(map.keys())+'|[0-9]))', line)
                         for line in lines]]


print("Solution DAY1-1: " + str(sum(get_digits(DATA))) )
print("Solution DAY1-2: " + str(sum(get_digits_and_translate(DATA2))) )
