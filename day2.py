import advent_of_code as aoc

import pandas as pd


## PART 1
num = 2
lines = aoc.input_readlines(num)
lines = [line.strip('\n') for line in lines]

num_valid = 0
for line in lines:
    try: 
        rules,letter,pw = line.replace(':','').split(' ') 
        rules_min = int(rules.split('-')[0])
        rules_max = int(rules.split('-')[1])
        pw_count = pw.count(letter)
    except:
        print(f"input of {line} was not as expected, something went wrong.")
        continue

    if (pw_count >= rules_min) and (pw_count <= rules_max):
        print(f'{line} is valid.')
        num_valid += 1
        
print(f"Answer: {num_valid}")


## PART 2
num_valid = 0
for line in lines:
    print(line)
    try: 
        rules,letter,pw = line.replace(':','').split(' ') 
        pos1 = int(rules.split('-')[0]) - 1 # convert to zero-index
        pos2 = int(rules.split('-')[1]) - 1 # convert to zero-index
    except:
        print(f"input of {line} was not as expected, something went wrong.")
        continue

    ## pos1 or pos2 of password must match letter. Both not allowed
    if (pw[pos1] == letter) and (pw[pos2] != letter):
        print(f'{line} is valid.')
        num_valid += 1
    elif (pw[pos1] != letter) and (pw[pos2] == letter):
        print(f'{line} is valid.')
        num_valid += 1
        
print(f"Answer: {num_valid}")
