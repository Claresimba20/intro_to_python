#lists[]:built in python data structure used to store multiple items in a single variable
#e.g students=["clare","sharon","shadrack"]
#xtics
#ordered:maintain their insertion order
#mutable:can be changed-added,removed or modified
#modifying the list
students=["clare","sharon","shadrack"]
#students[1]="nduti"
#print(students)
#adding
#students.append("nduti")
#print(students)
#removing
#students.remove("sharon")
#print(students)
#inserting in lists
#students.insert(1,"nduti")
#print(students)
#indexed
#allow duplicates
#student=["clare","sharon","shadrack","clare"]
#print(student)
#can hold mixed data types
#numbers=[1,0.5,"banana",True]
#print(numbers)
#accessing elements in a list:by indexing
#students=["clare","sharon","shadrack"]
#print(students[2])

#print(students[:3])
#accessing elements by slicing
#print(students[0:2])
#accessing all names
#print(students[:])
#accessing clare and shadrack-explain this
#print(students[::2])
#using step in slicing-explain
#converting strings into lists
#sentence= "I love love reading"
#words=sentence.split()
#print(words)
#built in functions
#length of a list
#students=["clare","sharon","shadrack"]
#print(len(students))
#numbers=[1,2,3,4,5,"banana"]
#print(max(numbers))
#print(min(numbers))

#print(sum(numbers))

#name=["clare","sharon","shadrack"]
#a=list(("clare","sharon","shadrack"))
#print(name)
#print(a)

#looping through elements

#c=[1,2,3,4,5,6,7,8]
#print(c[1:8:3])

#dictionaries
person={"name":"clare","age":20}
#print(type(person))
#print(person["age"])
#keys-name,age    values-clare,20    items-(name:clare),(age:20)
#print(person.keys())
#print(person.values())
#print(person.items())

#modifying the values
#person["age"]=33
#print(person["age"])

#removing a key value pair
#person.pop("age")
#print(person)

#get method
#print(person.get("name"))

#for i,j in person.items():
    #print(i,j)

students=  {
    "name": ["clare", "sharon", "shadrack"],
    "age": [10, 15, 20],
    "grade": ["A","B","C"]
}
#print(students)
#print(students.get("age"))
#print(students["name"][1])
#update age of clare
#students["age"][0]=12
#print(students)

#using update method
#students.update({"age":[23,27,40]})
#print(students)

#adding a new key value pair
#students["email"]="clare@gmail.com"
#print(students)

#remove grade
students

tusde
#tupples()
#person=("clare",20,"student")
#name,age,profession=person
#print(person)
#print(name)