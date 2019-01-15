def main():
    pass

operations ={
'+':lambda x,y:x+y,
'-':lambda x,y:x-y,
'*':lambda x,y:x*y,
'/':lambda x,y:x/y,
'^':pow
}

try:
    first= float(input ('First number:'))
    operation=input('Operation:')
    second= float(input('Second number:'))
    result=operations[operation](first,second)
except Valuerror:
    print('Incorect input')
except KeyError:
    print('Unsupported operation')
except ZeroDIvisionError:
    print('Division by zero')            
else:
    print('Result',result)    
