print("                                           Question No. = 1")
new = "a quick brown fox jumps over a little lazy dog."
word = 'a'

count = new.count(word)
print("The count is :" , count)


print("                                         Question No. = 2")
year = int(input("input a year : "))

if (year % 400 ==0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("input a month [1-12]: "))

if month in (1,3,5,7,8,10,12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
        month_length = 30

day = int(input("input a day [1-31] : "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else :    
         month += 1
print("the next date is [dd-mm-yyyy] %d-%d-%d." %(day, month , year))


print("                                     Question No. = 3")
my_list = [1,3,56,10,9,44,58,87]
print("The list is  ", my_list)
print("The resultant tuple is :")
my_result = [(val, pow(val,2)) for val in my_list]
print(my_result)

print("                                    Question No. = 4")
cgpa = float(input("Enter the cgpa of a Student : "))
if cgpa == 10:
    print("Your Grade is 'A+' and Outstanding Performance")
elif cgpa>=9 and cgpa<10:
    print("Your Grade is 'A' and Excellent Performance")
elif cgpa>=8 and cgpa<9:
    print("Your Grade is 'B+' and Very Good Performance")
elif cgpa>=7 and cgpa<8:
    print("Your Grade is 'B' and Good Performance")
elif cgpa>=6 and cgpa<7:
    print("Your Grade is 'C+' and Average Performance")
elif cgpa>=5 and cgpa<6:
    print("Your Grade is 'C' and Below Average Performance")
elif cgpa>=4 and cgpa<5:
    print("Your Grade is 'D' and Poor Performance")
    
else:
    print("!!!!!!!INVALID!!!!!!!")


print("                                         Question No. = 5")
n = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
for row in range(0,6):
    column = 0
    counter = 0

    while column<11:
        if column<row or column>11-row-1:
            print(" ", end="")

        else:
            print(n[counter], end="")
            counter = counter+1
        column = column+1
    print("")    


print("                                       Question No. = 6")

D = dict()

n = int(input("Details of how many students : "))

for i in range(1,n):
    x = input("Enter Name of a Student : ")
    y = int(input("Enter SIDs : "))
    D[y] = (x)
    print("A")
print(sorted(D.items() , key = lambda  item: item[1]))

print("B")
sorted_with_names = sorted(D.values())
print(f"sorted_names_values is {sorted_with_names}")
print("")

print("C")
sorted_with_SIDs = sorted(D.keys())
print(f"sorted_SIDs_key is{sorted_with_SIDs}")
print("")

print("D")
SID = int(input("enter SID whose details you want"))
if SID in D.keys():
          print(f"name of student {D[SID]}")
else:
    print(" details are not here")
print("")    
          
print("                                       Question No. = 7")
def fibonacciSeries(i):
    if i <=1:
        return i
    else:
        return (fibonacciSeries(i-1) + fibonacciSeries(i-2))

num = int(input("Enter a number:  "))
if num <=0:
    print("please enter a positive no")
else:
    print("Fibonacci Series:  ", end=" ")
    for i in range(num):
        print(fibonacciSeries(i), end=" ")


def fibo(n):
    if n<=1:
        return n
    else:
        res = fibo(n-1) + fibo(n-2)
        return res
sum = 0
for i in range(0,num):
    r = (fibo(i))
    sum += r
    print(r)

print("sum", sum)    


avg = sum/num
print(" avg is : " , avg)

print("                                      Question No. = 8")
set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}

print("A")
not_both = set1^set2
print(f"set with elements that is not common in both is {not_both}")

print("B")
only_in_one = set1^set2^set3
print(f"set of elements that is only present in 1 set is {only_in_one}")

print("C")
onlyin2  = (set1|set2|set3)-(set1^set2^set3)-(set1&set2&set3)
print(f"set of elements that is only present in 2 set is {onlyin2}")

print("D")
new = set()
for n in range(1,11):
    new.add(n)    
not_common = new - set1
print(f"set of all integers in the range 1 to 10 that are not in set1 {not_common}")

print("E")
new1 = set()
for n in range (1,11):
    new1.add(n)
not_common_1 = new1-(set1|set2|set3 )
print(f"set of all integers in the range 1 to 10 that are not in set1 and set2 and set3 is {not_common_1}")
