import csv
from random import randrange

def select_program():
    
    print('''
                KING'S PRAISE BV LIST GENERATOR
            What kind of program do you need this list for?
                    >> PROGRAM TYPES <<
            [1] Major/Special program (eg. Conference)
            [2] Normal program (eg. Midweek service)
        ''')
    
    program = input('>> ')
    return program
    
def bv_list(csv_file,program):
    tenors,altos,sopranos = [],[],[]
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if program == '1': #Major programs
                if row['Clan'] == 'Yes':
                    if row['Part'] == 'Tenor':
                        tenors.append(row['Name'])
                    elif row['Part'] == 'Alto':
                        altos.append(row['Name'])
                    elif row['Part'] == 'Soprano':
                        sopranos.append(row['Name'])
                        
            elif program == '2': #Normal programs
                if row['Clan'] == 'No':
                    if row['Part'] == 'Tenor':
                        tenors.append(row['Name'])
                    elif row['Part'] == 'Alto':
                        altos.append(row['Name'])
                    elif row['Part'] == 'Soprano':
                        sopranos.append(row['Name'])
    return [tenors,altos,sopranos]

def random_pick(tenors,altos,sopranos): #Passing the part lists as arguments
    x,y,z = len(tenors),len(altos),len(sopranos) # stores the length of the lists 
    a,b,c = randrange(x),randrange(y),randrange(z) # storing the random indices
    selected = [tenors[a],altos[b],sopranos[c]] # final bv_list from random indices
    return selected

def get_list(list):
    for i in list:
        print(i)

def menu():
    n = 0
    selected = []
    program = select_program()
    tenor,alto,soprano = bv_list('kp.csv',program)
    
    print('********************************')
    while n<3:
        if n == 0:
            print('>> WORSHIP <<')
        elif n == 1:
            print('>> PRAISE <<')
        elif n == 2:
            print('>> AUXILLIARY <<')
        print(' ')
        for i in selected:
            if i in tenor:
                tenor.remove(i)
            elif i in alto:
                alto.remove(i)
            elif i in soprano:
                soprano.remove(i)
        selected = random_pick(tenor,alto,soprano)
        get_list(selected)
        print('********************************')
        n += 1 













