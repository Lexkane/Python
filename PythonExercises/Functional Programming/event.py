def main():
    pass

handlers=[]
for i in range(1,4):
    def on_click(i=i):
        print("Button {} clicked".format(i))
    handlers.append(on_click)    

for handler in handlers:
    handler()            