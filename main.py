print("Hello World")

# Arithmetic Operators
num1 = 10
num2 = 3
print("num1 + num2 is", num1+num2)
print("num1 - num2 is", num1-num2)
print("num1 * num2 is", num1*num2)
print("num1 / num2 is", num1/num2)
print("num1 // num2 is", num1//num2)
print("num1 % num2 is", num1%num2)
print("num1 ** num2 is", num1**num2)

# strings
name = "Prateek"
print(name)
print(name[0:3]) #START FROM 0 TILL 2
# print(name[a:b]) #START FROM a TILL (b-1)
print(name.upper())
print(name.capitalize())
print(name.count("a"))

# user input
name1 = input("Enter your name:")
print(name1)

number = input("Enter a Number:")
print(type(number))
# by default input has a type of string
print(int(number)+6)

a1 = "Tanu" \
" is a good girl"
a2 = 'Ayush' \
' is a good boy'
# The below written both examples will only take first string in consideration
# a1 = "Tanu"
# " is a good girl"
# a2 = 'Ayush'
# ' is a good boy'
a3 = '''Bittu
She is a good girl'''
print(a1)
print(a2)
print(a3)

#  lists

l1 = [2,56,34523,33,3,33,"Prateek"]
print(l1)
print(type(l1))
l1.remove("Prateek") #it will only remove 1st instance of 33
print(l1)
print(len(l1))
l1.sort()  # Sort the list in-place
l1.append(1234)
print(l1)  # Print the sorted list

# tuples they are immutable
t1 = (3,78,95,132,653)
print(t1.count(78))
print(t1.index(95))

# sets (duplicates are not considered)
s1 = {2,6,6,6,7,99,4,6}
s2 = {2,8,99,4,8,0,12}
s1.pop() # randomly removes a no. from set
print(s1)
print(s1.union(s2))
print(s1.intersection(s2))

# Dictionaries
dict1 = {}
s3 =set()
print(dict1,type(dict1))
print(s3,type(s3))

dict2 = {"Prateek":65,"Tanu":95,"Dev":75,"Bhogesh":58,"Saurabh":31};
print(dict2["Saurabh"])

# if else

age = int(input("Enter your age: "))

if(age>18):
    print("Yes, you can drive")
elif(age==1):
    print("You are a kid")
elif(age==10):
    print("You are a decade kid")
else:
    print("No, you can go home")
print("End of the program")

# match case
m1 = int(input("Please enter a case no."))

match m1:
    case 1:
        print("Case is 1")
    case 2:
        print("Case is 2")
    case 3:
        print("Case is 3")
    case 4:
        print("Case is 4")
    case _:
        print("No case found")

# Write a python program to print table between 1 and 10
n = int(input("Enter a number: "))
if(0<=n<11):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
else:
    print("Enter a no. between 0 and 10")

#     Loop

for i in range(5):
    print(i+1)

s = {2,25,355,432,543,654,765,876,987,1098}
for i in s:
    print(i)


i=0
while(i<10):
    print(i+1)
    i+=1
print("End of the program...")

# Functions

def add(a,b):
    return print(a+b)

add(10,20)

def letterGenerator(name,date):
    st= f"Hii mam,\n This is {name} and I will not come to school on {date}"
    print(st)
letterGenerator("Prateek","26th May 2025")

# try except

try:
    a = int(input("Give a no.: "))
    print(a+3)
except Exception as e:
    print("some error occured",e)

    # file I/O
#     Writing in a file

s = "Prateek is an ugly boy"
# Method 1
# with open("test.txt","w") as f:
#     f.write(s)
# Method 2
f = open("test.txt","w")
f.write(s)
f.close()


#     Reading from a file
# Method 1
with open("Prateek.txt","r") as f:
    s= f.read()
    print(s)
# # Method 2
# f = open("test.txt","r")
# s= f.read()
# f.close()

#     Appending in a file (It does not clear already existing data while writing something

s = "Prateek is an ugly boy"
# Method 1
# with open("Prateek.txt","a") as f:
#     f.write(" but he is ugly too")
# Method 2
f = open("test.txt","a")
f.write(" but he is ugly too")
f.close()

# OOPS

class Emplyee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(f'My name is {self.name} and my salary is {self.salary}')

prateek = Emplyee("Prateek",10000000)
prateek.display()