import re
numberstr = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', }
print(sum([int((numberstr[line[0]] if line[0] in numberstr
                else line[0])+(numberstr[line[-1]] if line[-1] in numberstr
                                              else line[-1])) for line in
           [re.findall(r'(?=('+'|'.join(numberstr.keys())+'|[0-9]))', line) for line in open('inputs/day1')]]))