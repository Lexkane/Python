import sys

def main():
    pass

def is_palindrome(word):
  if len(word) == 1: return 'YES'
  if word[0] != word[-1]: return 'NO'
  return is_palindrome(word[1:-1])

def is_palindrom(s):
    length = len(s) 
    for i in range(int(length / 2)):
        if s[i] != s[length - i - 1]:
            return 'NO'
    return 'YES'

x=str(sys.argv[1]).lower().replace(" ","")  
print(is_palindrom(x))