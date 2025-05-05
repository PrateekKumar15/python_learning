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
