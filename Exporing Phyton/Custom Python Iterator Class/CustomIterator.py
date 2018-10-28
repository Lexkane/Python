#Custom Iterator class

import math
class MyRange :
    def __init__(self,first,second=None,step=1):
        if second is None:
            self.start=0
            self.end=first
        else:
            self.start=first
            self.end=second
        if step !=0:
            self.step=step
        else:
            raise ValueError("Step Cannot be zero")
        self.length=math.ceil((self.end-self.start)/self.step)
    def __len(self):
        return self.length
    def __getitem__(self,index):
        if 0<=index<len(self):
            return self.start+index*self.step
        else:
            raise IndexError("MyRange index out of range")
    def __repr__(self):
        return "MyRange({},{},{}".format(self.start,self.end,self.step)
    def __iter__(self):
        return RangeIterator(self)

class RangeIterator:
        def __init__(self,range_instance):
            self.range=range_instance
            self.current_value=None
            self.next_value=range_instance.start
        def __iter__(self):
            return self
        def __next__(self):
            if (self.next_value)>=self.range.end  and self.range.step>0 or \
             self.next_value <= self.range.end and self.range.step<0:
              raise StopIteration
            result= self.next_value
            self.next_value+=self.range.step
            return result                      