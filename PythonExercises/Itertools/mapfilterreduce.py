from functools import reduce

def main():
    pass

values=[2,1,5,8,3,2]

for square in map (lambda x:x**2,values):
    print(square)

positive=list(filter(lambda x:x>0,values))    
print(positive)

product=reduce(lambda x,y:x*y,values)
print(product)