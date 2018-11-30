def main():
 pass
 
def fib(n):
  a,b=1,1
  for i in range(n-1):
   a,b=b,a+b
  return a
 
def fibR(b):
   if n==1 or n==2:
     return 1
   return fibR(n-1)+fibR(n-2)

a,b=0,1
def fibI():
   global a,b
   while True:
     a,b=b, a+b
     yield a

def memoize (fn,arg):
   if arg not in memo:
     memo[arg]=fn(arg)
   return memo[arg]

 
class Memoize:
  def __init__(self,fn):
   self.fn=fn
   self.memo={}
  def __call__(self,arg):
    if arg not in self.memo:
     self.memo[arg]=self.fn(arg)
    return self.memo[arg]

@Memoize  
def fib(n):
  a,b=1,1
  for i in range(n-1):
    a,b= b,a+b
  return a 
print fib(5)  