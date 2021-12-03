import advent_of_code as aoc

import pandas as pd


## PART 1
num = 1
lines = aoc.input_readlines(num)


entries = [int(line) for line in lines]
SUMM = 2020
stop = 0
for entry in entries:
    #print(entry)
    if stop:
        ## Two numbers that sum to SUMM have been found
        continue

    ## Drop entry from entries, won't need it for comparing any more numbers
    entries.pop(0)
    for i_entry in entries:
        if (entry + i_entry) == SUMM:
            a = entry
            b = i_entry
            stop = 1
print(f"Answer: {a*b}")


## PART 2
entries = [int(line) for line in lines]
SUMM = 2020
stop = 0
for entry in entries:
    print(entry)
    if stop:
        ## Two numbers that sum to SUMM have been found
        continue

    ## Drop entry from entries, won't need it for comparing any more numbers
    entries.pop(0)
    for i_entry in entries:
        for j_entry in entries:
            if (entry + i_entry + j_entry) == SUMM:
                a = entry
                b = i_entry
                c = j_entry
                stop = 1
print(f"Answer: {a*b*c}")
