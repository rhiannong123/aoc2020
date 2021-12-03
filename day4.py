import advent_of_code as aoc
import pandas as pd
import numpy as np

num = 4
lines = aoc.input_readlines(num)
lines = [line.strip('\n') for line in lines]


## PART 1
EXPECTED_KEYS = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid',
]

CID_OPTIONAL = [ikey for ikey in EXPECTED_KEYS if 'cid' not in ikey]

passports = []
passport = {}
for line in lines:
    
    if line == '':
        passports.append(passport)
        passport = {}
        continue

    # example line = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd'
    line_split = line.split(' ')
    
    # example line_split = ['ecl:gry','pid:860033327','eyr:2020','hcl:#fffffd']
    for parameter in line_split:
        #example parameter = 'ecl:gry'
        
        key,value = parameter.split(':')
        passport[key] = value
passports.append(passport)

num_valid = 0
for passport in passports:
    print(passport)
    passport_check_cid_opt = [ikey in passport for ikey in CID_OPTIONAL]
    if all(passport_check_cid_opt):
        num_valid += 1

print(f'Answer: {num_valid}')



## PART 2

def check_year(year,ytype):

    try:
        year = int(year)
    except:
        print('f{year} of {ytype} could not be converted, returning False.')
        return False
    
    if ytype == 'byr':
        return (year <= 2002) and (year >= 1920) 
    elif ytype.lower() == 'iyr':
        return (year >= 2010) and (year <= 2020)
    elif ytype.lower() == 'eyr':
        return (year >= 2020) and (year <= 2030)

def check_hgt(height):
    ''' Return True if units cm or in given and values in acceptable range
        Input = string "181cm" or "62in"
    '''
    
    info = {}
    
    if ('cm' in height):
        try:
            height = int(height.replace('cm',''))
            info['unit'] = 'cm'
            info['min'] = 150
            info['max'] = 193
        except:
            print(f'Could not drop unit and convert to int, input is weird: {height}. Try again, returning False.')
            return False
    elif ('in' in height):
        try:
            height = int(height.replace('in',''))
            info['unit'] = 'in'
            info['min'] = 59
            info['max'] = 76

        except:
            print(f'Could not drop unit and convert to int, input is weird: {height}. Try again, returning False.')
            return False

    else:
        print('height must contain "cm" or "in". Returning False')
        return False

    return (height <= info['max']) & (height >= info['min'])    
    

def check_hcl(hcl):
    ''' Return True if input is # followed by exactly six characters 0-9 or a-f.
    '''
    
    if isinstance(hcl,str) == False:
        print('input must be string! Try again, returning False.')
        return False
    
    six_char_good = list('0123456789abcdef')
    
    return (hcl[0] == '#') & set(hcl[1:]).issubset(set(six_char_good)) & (len(hcl) == 7)

def check_ecl(ecl):
    '''Return true if exactly one of: amb blu brn gry grn hzl oth.
    '''

    eye_colors = ['amb','blu','brn','gry','grn','hzl','oth']
    
    if isinstance(ecl,str) == False:
        print('input must be string! Try again, returning False.')
        return False
    
    return (ecl.lower() in eye_colors)

def check_pid(pid):
    ''' Return True if: pid (Passport ID) - a nine-digit number, including leading zeroes.
    '''
    
    if len(pid) != 9:
        print('Incorrect number of digits in pid. Returning False.')
        return False
    
    try:
        pid = int(pid)
        return True
    except:
        print(f'Could not convert to int, input is weird: {pid}. Try again, returning False.')
        return False

def get_and_run_check(ilist):
    '''ilist[0] = expected_fields value
       ilist[1] = entry for that expected field
    '''
 
    if ilist[0].lower() in ['byr','iyr','eyr']: 
        return check_year(ilist[1], ilist[0])
    elif ilist[0].lower() in 'hgt':
        return check_hgt(ilist[1])
    elif ilist[0].lower() in 'hcl':
        return check_hcl(ilist[1])
    elif ilist[0].lower() in 'ecl':
        return check_ecl(ilist[1])
    elif ilist[0].lower() in 'pid':
        return check_pid(ilist[1])
    elif ilist[0].lower() in 'cid':
        return True # doesn't matter
    else:
        print('do not recognize input type: ', ilist)


passports = []
passport = {}
for line in lines:
    
    if line == '':
        passports.append(passport)
        passport = {}
        continue

    # example line = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd'
    line_split = line.split(' ')
    
    # example line_split = ['ecl:gry','pid:860033327','eyr:2020','hcl:#fffffd']
    for parameter in line_split:
        #example parameter = 'ecl:gry'
        
        key,value = parameter.split(':')
        passport[key] = value
passports.append(passport)

num_valid = 0
for passport in passports:
    if all(field in passport for field in CID_OPTIONAL):
        status = True
        passport_list_of_lists = list(passport.items())
        for ilist in passport_list_of_lists:
            if status == False:
                continue
            status = get_and_run_check(ilist)
        if status == True:
            num_valid += 1

print(f'Answer: {num_valid}')
