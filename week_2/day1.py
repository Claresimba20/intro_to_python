greeting="hello"
#print(greeting)
#print(greeting.upper())
#print(greeting.lower())

name="clare"
age=21
#print(f"My name is{name} and I am {age} years old")
#print(len(name))
#print("b" in name)
#print("b" not in name)

#r=read mode
#a=append
#w=write
#x=create

opened_file=open(r"C:\Users\User\Desktop\python_programming2\week_2\quotes.txt","r")
content=opened_file.read()
#print(content)

with open(r"C:\Users\User\Desktop\python_programming2\week_2\quotes.txt","r") as opened_file:
    content=opened_file.read()
    #print(content)

with open(r"C:\Users\User\Desktop\python_programming2\week_2\quotes.txt","r") as opened_file:
    content=opened_file.readline()
    #print(content[2])

with open(r"C:\Users\User\Desktop\python_programming2\week_2\demo_writing_file.txt","w") as f:
    f.write("we re demonstrating the writing mode in files")
#concatenation
name="clare"
greeting="hello"
#print(name+greeting)
#repetion
complete=name+" "+greeting
#print(complete)

repeat_greeting=greeting*3
#print(repeat_greeting)


#slicing
#print(greeting[:3])
#print(greeting[2:])

#print(greeting[2:4])

#negative indexing/reverse indexing
#right to left in the array
#starts from -1
#the step size should be negative


greeting="hello"
#print(greeting[-1:-4:-1])

fruits=("orange","mango","banana","apple","lemon")
#print(fruits[-2:-4:-1])

#print(fruits[-1:-4])

file_name="myfile.txt"

with open("myfile.txt","x") as file:
    file.write("Hello Clare.\n")
#with open("myfile.txt","r") as file:
    #content=file.read()
    #print(content)



