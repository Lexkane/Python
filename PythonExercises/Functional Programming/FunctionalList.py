def main ():
    pass

elem=lambda value,next:{'value':value,'next':next}
to_string=lambda head :'' if head is None\
 else str(head['value']) +''+ to_string(head['next'])
values=elem(1,elem(2,elem(3,None)))
print(to_string(values))                        