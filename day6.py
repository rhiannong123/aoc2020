import advent_of_code as aoc
import pandas as pd
import numpy as np


num = 6
lines = aoc.input_readlines(num)
lines = [line.strip('\n') for line in lines]


## PART 1
## Count number of questions (each unique letter in group)
## First build up groups, separated by skipped lines

groups = []
group = ''
for line in lines:
    if line == '':
        ## End of group found, append groups and start afresh
        groups.append(group)
        group = ''
    else:
        ## Group continues
        group = group + line

if group != '':
    groups.append(group)

yess = [len(set(group)) for group in groups]
print(f"Answer: {sum(yess)}")


## PART 2
## Redefine groups with comma separating each person in each group
groups = []
group = ''
for line in lines:
    if line == '':
        ## End of group found, append groups and start afresh
        groups.append(group)
        group = ''
    else:
        ## Group continues
        group = group + line + ','

if group != '':
    groups.append(group)

## Only count number of questions that everyone in a group answered    
yess = [] 
for group in groups: 
    people = group.split(',')[:-1] # drop last "person" that is a result of comma at end
    if len(people) == 1:
        ## CASE group of 1 so every question answered is counted
        answers = len(people[0]) 
        yess.append(answers) 
    else:
        ## CASE: Multiple peeps in group, initialize answers to compare
        answers = list(people[0])

        ## For each person in group,
        ##  compare current answer with previous and only keep common answers
        for person in people[1:]: 
            answers = list(set(list(person)).intersection(answers)) 
        yess.append(len(answers)) 
  
print(f"Answer: {sum(yess)}") 
   

