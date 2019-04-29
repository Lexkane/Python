def main():
	pass

open ("pickled_list.p","wb") as MyFile:
pickle.dump(MyObject,Myfile)	

import pickle

MyObject=["a list","containing",5,"values including another list",["inner","list"]]

with open ("pickled_list.p","wb") as MyFile:
	pickle.dump(MyObjec,MyFile)

with open("pickled_list.p","rb") as MyFile:
	MyNewObject=pickle.load(MyFile)