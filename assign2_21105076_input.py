print("                              Question No. = 1")
new = "Python is a case sensitive language"

print("                           1.a")
print(len(new))

print("                          1.b")
reversed = ''.join(reversed(new))
print(reversed)

print("                           1.c")
print(slice(new[10:26]))

print("                           1.d")
new1 = new.replace("a case sensitive", "object oriented")
print("replaced = ", new1)

print("                           1.e")
print("Index of substring 'a':", new.index('a'))

print("                           1.f")
n = new.replace(" ", "")
print("Removed white spaces from 'new' :", n)

print("                               Question No. = 2")
name = "Hey, {} Here!".format("CHIRAG GUPTA")
print(name)
SID = "My SID is {}".format("21105076")
print(SID)
info = "I am from {department} and my CGPA is {cgpa}".format( department = "ECE", cgpa= "8.3")
print(info)

print("                            Question No. = 3")
a = 56
b = 10

print("                                3.a")
print(a&b)

print("                                3.b")
print(a|b)

print("                                3.c")
print(a^b)

print("                                3.d")
print("Left shift a with 2 bits and left shift b with 2 bits ",a<<2 , b<<2)

print("                                3.e")
print("right shift a with 2 bits and right shift b with 4 bits ",a>>2 , b>>4)

print("                    Question No. = 4")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 > num2) and (num1 >num3):
    largest = num1
elif (num2 > num1) and (num2 > num3):
    largest = num2
else:
    largest = num3

print("the largest number is", largest)

print("                       Question No. = 5")
CG = "My name is CHIRAG GUPTA"
if "name" in CG:
    print("YES")
else:
    print("NO")

print("                          Question No. = 6")
a = int(input("Enter first length : "))
b = int(input("Enter second length : "))
c = int(input("Enter third length : "))
sum = (a + b + c)
if a or b or c > sum:
    print("YES")
else:
    print("NO")



        

