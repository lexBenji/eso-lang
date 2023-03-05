#!/usr/bin/env python3

from sys import argv
import random

dr=None

class DirectionError(Exception):
    pass

print(argv)

if len(argv) < 2:
    raise BufferError('Not enought argument')
elif not argv[1].endswith('.esol'):
    raise BufferError('Not an ESOL file')
elif len(argv) == 3:
    if not argv[2].lower() in ['right','left','up','down']:
        raise DirectionError('Not a valid direction')
    else:
        dr=argv[2].lower()

y=0
x=0
drs=[
'up',
'right',
'down',
'left'
]

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
        print(dr)
        print(f[y][x])
        if cell[i] < 0:
            cell[i] = 0
        if f[y][x] == '>':
            if i > len(cell)-1:
                i = 0
            else:
                i+=1
            dr='right'
        elif f[y][x] == '<':
            if i < 0:
                i=len(cell)-1
            else:
                i=i-1
            dr='left'
        elif f[y][x] == '^':
            cell[i]+=1
            dr='up'
        elif f[y][x] == 'v':
            cell[i]=cell[i]-1
            dr='down'
        elif f[y][x] == 'E':
            break
        if dr == 'right':
            if (x+1) > (len(f[y])-1):
                raise PointerError('Pointer Cannot Continue')
            else:
                x=x+1
        elif dr == 'left':
            if (x-1) < 0:
                raise PointerError('Pointer Cannot Continue')
            else:
                x=x-1
        elif dr == 'up':
            if (y-1) < 0:
                raise PointerError('Pointer Cannot Continue')
            else:
                y=y-1
        elif dr == 'down':
            if (y+1) > (len(f)-1):
                raise PointerError('Pointer Cannot Continue')
            else:
                y=y+1
        elif dr == None:
            dr = random.choice(drs)

for c in cell:
    if c == 0:
        pass
    else:
        if outt == True:
            print(chr(c),end='')
        else:
            print('{0:2}:{1:3}'.format(cell.index(c),c))
