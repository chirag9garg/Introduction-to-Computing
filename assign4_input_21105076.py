print("                   Question No. = 1")
def TowerOfHanoi(n , source , destination , auxiliary):
    if n==1:
        print("Move disk 1 from source" , source , "to destination" , destination)
        return
    TowerOfHanoi(n-1 , source , auxiliary , destination)
    print("Move disk" , n , "from source" , source , "to destination" , destination)
    TowerOfHanoi(n-1 , auxiliary , destination , source)



n = 3
TowerOfHanoi(n , 'A' , 'B' , 'C')

print("                       Question No. = 2")
n = int(input("Enter no. of rows"))
a = []
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1] + a[i-1][j])
    if (n != 0):
         a[i].append(1)
for i in range(n):
    print("  "*(n-1),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
    print()    

print("                             Question No. = 3")
print(" ")
a=int(input("Enter the first integer: "))
b=int(input("Enter the second integer: "))
c=a%b
d=a//b
print("Remainder is: ", c)
print("Quotient is: ",d)

print("A")
print(callable(c))
print(callable(d))

print("B")
if(c!=0):
    if (d!=0):
        print("Both values are non zero")
    else:
        print("One value is zero")
else:
    if (d!=0):
        print("One value is zero")
    else:
        print("Both values are zero")

print("C")
set1=set()
for i in range (4,7):
    f=c+i
    g=d+i
    if(f>4):
        set1.add(f)
        print(set1)
    if(g>4):
        set1.add(g)
        print(set1)
print("D")
print(set())
print("E")
print(set1)
set2 = frozenset(set1)
print("IMMUTABLE SET ; " , frozenset(set1))

print("F")
print("Largest value in the set: ", max(set2))
k=max(set2)
print("Hash value: ", hash(k))
print("")

print("                             Question No. = 4")
class Student:
    def __init__(self , name , rollno):
        self.name = name
        self.rollno = rollno
    def displayDetails(self):
        print("Name : " , self.name , "Roll No." , self.rollno)

    def __del__(self):
        print("OBJECT DESTROYED")    

    

s1 = Student("A" ,1)
s2 = Student("B" , 2)
s3 = Student("C" , 3)
s4 = Student("D" , 4)

print("Details of all Employes")
s1.displayDetails()
s2.displayDetails()
s3.displayDetails()
s4.displayDetails()


del s1
print("")

print("                             Question No. = 5")
class Employee:
        def __init__(self, name, salary):
            self.name=name
            self.salary=salary
        def displayDetails(self):
            print("Name:", self.name, ", Salary:", self.salary)

        def __del__(self):
            print("RECORD DELETED")

            
e1=Employee("Mehak",  40000)
e2=Employee("Ashok",  50000)
e3=Employee("Viren",  60000)

print("Details of all employee:")
e1.displayDetails()
e2.displayDetails()
e3.displayDetails()

print("A")
e1.salary = 70000
print(e1.salary)

print("B")
del e3
print("")


print("                Question No. = 6")
print("")
word = input("Enter the first word :  ")

testword = input("Enter a new meaningful word to test your friendship: ")


def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count


if count_in_dict(word) != count_in_dict(testword):
    print("")

def userinput():
    ans = input("\nDoes the word makes sense?(y or n)\n")

    if ans == 'y':
        print("The friends pass the friendship test!!\n\n")
    elif ans == 'n':
        print("The word doesn't have a meaning, friendship is fake!!\n\n")
    else:
        print("Invalid input, try again")
        userinput()

userinput()
print("")        
