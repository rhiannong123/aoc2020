import advent_of_code as aoc
import pandas as pd
import numpy as np


num = 3
lines = aoc.input_readlines(num)
lines = [line.strip('\n') for line in lines]


## PART 1

maxstr = len(lines[0]) 
num_trees = 0 
for idx,line in enumerate(lines): 
    ## Slope of right 3, down 1
    check = idx*3

    ## subtract whole iterations off to circle back
    check_ind = check - int(np.floor(check/(maxstr)))*maxstr 
    
    ## Check for tree
    if line[check_ind] == '#': 
        num_trees +=1 
print(f"Answer: {num_trees}")


## PART 2


maxstr = len(lines[0])
slopes = [
    {'right': 1, 'down': 1},
    {'right': 3, 'down': 1},
    {'right': 5, 'down': 1},
    {'right': 7, 'down': 1},
    {'right': 1, 'down': 2},
     ]
total_num_trees = []
for slope in slopes:
    
    num_trees = 0
    cursor = -1
    for idx,line in enumerate(lines): 

        if idx % slope['down'] != 0:
            cursor = cursor
            continue
        else:
            cursor += 1
        
        check = cursor * slope['right']

        ## subtract whole iterations off to circle back
        check_cursor = check - int(np.floor(check/(maxstr)))*maxstr 

        ## Check for tree
        if line[check_cursor] == '#': 
            num_trees +=1

    ## Increment total trees
    total_num_trees.append(num_trees)
    print(f'For a slope of {slope}, number of trees: {num_trees}')
          
print(f"Answer: {np.product(total_num_trees)}")
