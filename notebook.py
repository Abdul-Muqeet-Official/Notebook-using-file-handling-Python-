print("*"*20,"The NoteBook","*"*20,"\n")
path='c:/pop/notebook.txt'

def view():
	with open(path,'r')as file:
		data=[]
		# print(file.readlines())
		# file.readlines()
		print("/"*20)
		
		for i in file:
			data.append(i)

		print(data)
		print(len(data))

		data1=[]
		for i in range (len(data)):
			if data[i]=="\n":
				print("slicing-------------------",i)
				data1.append(data[0:i])

			
		print("*"*50)				
		print(data1)

view()

x=input("what do you want to write :")

with open(path,'a')as file:
	file.write(x+"\n")

data=view()


