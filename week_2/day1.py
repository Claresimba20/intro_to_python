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
