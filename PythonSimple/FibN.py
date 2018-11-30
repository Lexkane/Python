import sys;
import math;

def main():
    pass

x=int(sys.argv[1])
fi=((1+math.sqrt(5))/2)
val=((fi**x)-(-fi)**(-x))/(math.sqrt(5))
print(int(val))