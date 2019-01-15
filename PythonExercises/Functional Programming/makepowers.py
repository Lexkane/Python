def main():
    pass

def make_powers(count):
    powers=[]
    for i in range(count):
        powers.append((lambda p:lambda x:x**p)(i))
    return powers

powers=make_powers(5) 
for power in powers:
 print(power(2))