#!/usr/bin/env python3

from sys import argv
import random

if len(argv) < 2:
    raise BufferError('Not enought argument')
elif not argv[1].endswith('.esol'):
    raise BufferError('Not an ESOL file')

y=0
x=0
drs=[
'k',
'l',
'j',
'h'
]
dr = random.choice(drs)

cell=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i=0
outt=False

class PointerError(Exception):
    pass

with open(argv[1]) as rf:
    rf=rf.readlines()
    if rf[0] == '@text\n':
        outt=True
    else:
        outt=False
    f=[list(x) for x in rf]
    for j in f:
        if 'S' in j:
            y = f.index(j)
        else:
            pass
    x=f[y].index('S')
    while True:
        if f[y][x] == '>':
            if i > len(cell)-1:
                i = 0
            else:
                i+=1
            dr='l'
        elif f[y][x] == '<':
            if i < 0:
                i=len(cell)-1
            else:
                i=i-1
            dr='h'
        elif f[y][x] == '^':
            cell[i]+=1
            dr='k'
        elif f[y][x] == 'v':
            cell[i]=cell[i]-1
            dr='j'
        elif f[y][x] == 'E':
            break
        if dr == 'l':
            if (x+1) > (len(f[y])-1):
                raise PointerError('Pointer Cannot Continue')
            else:
                x=x+1
        elif dr == 'h':
            if (x-1) < 0:
                raise PointerError('Pointer Cannot Continue')
            else:
                x=x-1
        elif dr == 'k':
            if (y-1) < 0:
                raise PointerError('End of line')
            else:
                y=y-1
        elif dr == 'j':
            if (y+1) > (len(f)-1):
                raise PointerError('End of line')
            else:
                y=y+1

for c in cell:
    if c == 0:
        pass
    else:
        if outt == True:
            print(chr(c),end='')
        else:
            print(cell.index(c),':',c)
