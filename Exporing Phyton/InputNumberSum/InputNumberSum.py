#Print sum of input integers as argument
import sys
def sum_digits(digit):
    return sum(int(x) for x in digit if x.isdigit())
def main():
  try:
     digit_string = sys.argv[1]
     print(sum_digits(digit_string))
  except:  IOError
if __name__=="__main__" :
  main()
