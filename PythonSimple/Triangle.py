import sys;

def main():
    pass


x=float(sys.argv[1])
y=float(sys.argv[2])
z=float(sys.argv[3])

if x<y+z and y<x+z and z<x+y : print('triangle')
else: print('not triangle')