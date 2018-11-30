import math;



def main():
    pass

value= input()
x, m, s = value.split(',')
x,m,s= float(x),float(m),float(s)

print ((1/(s*math.sqrt(2*math.pi)))*math.pow(math.e,-(x-m)*(x-m)/(2*s*s))) ;


if __name__ == '__main__':
    main()