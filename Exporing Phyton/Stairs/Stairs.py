#Print  stairs for input number 
import sys
def main():
  try:
    digit_string = int(sys.argv[1])
    for x in range (digit_string+1):
        if x!=0: print((digit_string-x)*(" ")+(x)*('#'))
        else :pass 
    for i in range(digit_string):
      print(" " * (digit_string - i - 1), "#" * (i + 1), sep="")
  except:IOError        
if __name__=="__main__" :
  main()
