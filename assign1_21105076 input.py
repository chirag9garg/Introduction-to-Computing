print("             Question 1")
number1 = int(input("enter first number"))
number2 = int(input("enter second number"))
number3 = int(input("enter third number"))
sum = (number1 + number2 + number3)
avg = sum/3
print(avg)

print("              Question 2")
tax_rate=int(0.20)
standard_deduction=int(10000)
additional_deduction=int(3000)
gross_income=int(input("enter income"))
no_of_dependents=int(input("enter depents"))
taxable_income=gross_income-standard_deduction-(additional_deduction*no_of_dependents)
tax=taxable_income*tax_rate
print(tax)

print("           Question 3")
print("Student = [SID, Name, Gender, Dept. Name, CGPA]")
# 'M', 'F', 'U' is for Male, Female, Unkown
Student = [21105076, 'Chirag Gupta','M', 'ECE', 9.0]
print(Student)


print("      Question 4")
print("marks of five students")
marks= [89,50,65,100,33]
print("marks before sorting", marks)
marks.sort()
print("marks after sorting", marks)

print("                                            Question 5(a)")
color=['red', 'green', 'white', 'black', 'pink', 'yellow']
color.pop(3)
print(color)

print("                                            Question 5(b)")
color=['red', 'green', 'white', 'black', 'pink', 'yellow']
color.pop(3)
print(color)
color.pop(3)
print(color)
color.insert(3,'purple')
print(color)
