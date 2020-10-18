#!/usr/bin/env python3

'''
H:向前移动
J:向上移动 
K:向下移动 
L:向后移动 
'''
from filterpy.gh import GHFilter

f = GHFilter(x=0., dx=0., dt=1., g=.8, h=.2)
f.update(z=1.2)

print("f.update = ", f.update(z=1.2))
print("f.x = ", f.x, ";", "f.dx = ", f.dx)
print(f.update(z=2.1, g=.85, h=.15))










