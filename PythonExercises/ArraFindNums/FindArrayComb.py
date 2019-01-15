import itertools
import sys

def main():
    pass

def find_pairs(L,sum):
    s=set(L)
    edgeCase=float(sum)/2
    if L.count(edgeCase)==2:
        print(edgeCase,edgeCase)
    s.remove(edgeCase)
    for i in s:
        diff=sum-i
        if diff in s:
            print (i,diff)    

listone=list(sys.argv[1])
uniquelist=set(listone)
targetsum=sys.argv[2]
for n in itertools.combinations(uniquelist,2):
 if n[0]+n[1]==targetsum:
  print (str(n[0]+" "+n[1]))

#print(find_pairs(listone,targetsum))




