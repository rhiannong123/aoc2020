import advent_of_code as aoc
import pandas as pd
import numpy as np


num = 5
lines = aoc.input_readlines(num)
lines = [line.strip('\n') for line in lines]


## PART 1

FRONTBACK = ['F','B']
LEFTRIGHT = ['L','R']
ROWS = range(128)
COLS = range(8)

def get_row_or_col(line_substr,row_or_col,verbose=False):
    if row_or_col == 'row':
        row = list(ROWS)
        lower_half_letter = 'F'
    else:
        row = list(COLS)
        lower_half_letter = 'L'
        
    for letter in line_substr:
        if verbose:
            print(row)
        remaining_row_half = int(len(row)/2)
        if letter == lower_half_letter:
            row = row[0:remaining_row_half]
        else:
            row = row[remaining_row_half:]
    return row


max_seat = 0
for line in lines:
    # First 7 of line should be F or B, last 3 should be L or R
    fb = list(line[:7])
    lr = list(line[-3:])
    if (not set(fb).issubset(FRONTBACK)) or (not set(lr).issubset(LEFTRIGHT)):
        print('Input not as expected, Letter(s) found that arent F,B')
        continue

    row = get_row_or_col(fb, 'row')
    col = get_row_or_col(lr, 'col')
    seat = row[0] * 8 + col[0]
    
    print(seat, row, col)
    if seat > max_seat:
        max_seat = seat
        
print(f"Answer: {max_seat}")


## PART 2


seats = []
for line in lines:
    # First 7 of line should be F or B, last 3 should be L or R
    fb = list(line[:7])
    lr = list(line[-3:])
    if (not set(fb).issubset(FRONTBACK)) or (not set(lr).issubset(LEFTRIGHT)):
        print('Input not as expected, Letter(s) found that arent F,B')
        continue

    row = get_row_or_col(fb, 'row')
    col = get_row_or_col(lr, 'col')
    seat = row[0] * 8 + col[0]
    
    print(seat, row, col)

    seats.append(seat)
    
seat_found = False
for iseat in range(1, max_seat):
    if not seat_found:
        if iseat not in seats:
            if iseat-1 in seats:
                if iseat+1 in seats:
                    print(f"Found my seat: {iseat}!")
                    seat_found = True
    
print(f"Answer: {max_seat}")


