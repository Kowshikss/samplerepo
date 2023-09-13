#!/usr/bin/env python
# coding: utf-8

# # 1) Manipulate using a list:
#    1. to add new elemets to end of the list
#    2. to reverse elements in the list
#    3. to display same list of elements in the list
#    4. to concatenate two list
#    5. to sort the elements in the list ascending order

# In[1]:


ls=[1,2,3,4]
ls


# In[5]:


#1 to add new elemets to end of the list
ls.append(100) #append is used to add single element at end of the list.

#to add multiple elements extend
ls.extend([25,30,200])
print("after added listed elements are",ls)


# In[9]:


#2 to reverse elements in the list
ls = [1, 2, 3]
ls.reverse()  # Reverses the elements in the list
print("after reverse the elements are",ls)


# In[18]:


#3 to display same list of elements in the list
ls= [1,2,3,80,40,50]
print('the elements printed multiple times:',ls) 


# In[14]:


#4 to concatenate two list
ls1= [1, 2, 3]
ls2 = [4, 5, 6]
concatenated_ls = ls1+ls2  # Using the + operator # or
ls.extend(ls2)  # Using the extend() method
print("after concatenation my two list",ls)


# In[13]:


#5 to sort the elements in the list ascending order
ls = [3, 1, 2, 5, 4]
ls.sort()  # Sorts the list in ascending order in-place
print("ascending",ls)


# # Python program to do in tuples
#    1. Manipulate using tuples 
#    2. to add new elemets to end of the tuples
#    3. to reverse elements in the list
#    4. to display elements of same tuples in different times
#    5. to concatenate two tuples
#    6. to sort the elements in the tuples ascending order
#    

# In[17]:


#1 Manipulate using tuples 
tu=(1,5,6,'xyz',20,50)
tu


# In[11]:


#2 to add new elemets to end of the tuples

tu2=('apple',100)
tu1=(30,'yz',99)
tuple=tu1 + tu2
print('after add a new element:',tuple)


# In[21]:


#3 to reverse elements in the list
tuple=([30, 'yz', 99, 'apple', 100]) 

tuple.reverse()

print('reverse element:',tuple)


# In[13]:


#5 to concatenate two tuples

tuple1=(30, 'yz', 99, 'apple', 100)
tuple2=(60,44,'blue',2,100)

tuple=tuple1+tuple2
print(tuple)


# In[14]:


#6 to sort the elements in the tuples ascending order

tuple=[5,2,3,1,4]
tuple.sort()
print(tuple)


# In[25]:


#4 to display elements of same tuples in different times

tuple=(30, 'yz', 99, 'apple', 100)*5

print(tuple)


# # 3.Write a python program to implement the following using list

# In[ ]:


#1) Create a list with integers(min 10 numbers)

lst=[10,22,32,54,64,18,78,2,1,22]


# In[31]:


#2) Display list number in the list
lst=[10,22,32,54,64,18,78,2,1,22]
lst[-1:]


# In[32]:


#3 display the value from the list[0:4]
lst=[10,22,32,54,64,18,78,2,1,22]
lst[0:4]


# In[33]:


#4 display the value from the list[2:]

lst=[10,22,32,54,64,18,78,2,1,22]
lst[2:]


# In[34]:


#5 display the value from the list[:6]
lst[:6]


# # 4 . Write a python program:
#  
#   #tuple1=(10,30,40,60,70)
#   
# 

# In[39]:


#1) Display the element 10 and 50 from tuple1

tuple1=(10,30,40,60,70,80)
    
tuple1[0:2]


# In[38]:


#2) display the length of tuple1
tuple1=(10,30,40,60,70,80)

len(tuple1)


# In[40]:


#3) find minimum element from length of tuple1

tuple1=(10,30,40,60,70,80)
min(tuple1)


# In[41]:


#4) to add all element in the tuple1

tuple1=(10,30,40,60,70,80)
sum(tuple1)


# In[47]:


#5) to display the same tuple1 multiple times

tuple1=(10,30,40,60,70,80)

tuple=tuple1 * 10
print(tuple)


# # 5. Write python program

# In[48]:


#1)to calculate the length of string

string='Hello kowshik'

len(string)


# In[2]:


#2) reverse word in string

string='Hello kowshik'

string[::-1]


# In[51]:


#3)to display the same string multiple times

str= string * 5

print(str)


# In[52]:


#4)to concatenate two strings

str1='i am kowshik'
a=string +" "+str1
print(a)


# In[53]:


#5) str1="South India",using string slicing to display"India"

str1='South India'
str1[6:11]


# # 6) Perform the following

# In[3]:


#1)Creating the dictionary

dictionary={'name':'kowshik','age':23,'place':'neyveli'}

print("dictionary:",dictionary)


# In[4]:


#2)accesing values and keys in dictionary

dictionary.values()


# In[6]:


dictionary.keys()


# In[8]:


#3) updating the dictionary using a function

dictionary.update({'name':'Kowshik'})
print(dictionary)


# In[9]:


#4) clear and delete the dictionary values

dictionary.clear() 
 
print(dictionary) 


# # 7) python program to insert a number to any position in a list

# In[17]:


list = ['1','2', '8','14','50']
list.insert(0, '10')
print(list)


# # 8) python program to delete an element  from a list to index

# In[18]:


list = [14, 6, 8, 7, 6, 9, 2, 1, 10, 18]

del list[5]

print(list)


# # 9)write a program to display a number from 1 to 100

# In[20]:


i = 1
while i <= 100:
    print(i, end=" ")
    i += 1


# # 10) Write a python program to find sum of all items in tuple 

# In[23]:


tuple = (10, 20, 30, 80, 7)

result = sum(tuple)
print(result)  


# # 11) Define the dictionary with lambda functions

# In[20]:


# Define the dictionary with lambda functions

func_dict = {
    'Square': lambda x: x**2,
    'Cube': lambda x: x**3,
    'Squareroot': lambda x: x**0.5
}


num = float(input("Enter a number: "))


result = 0

for func_name, func in func_dict.items():
    output = func(num)
    result += output
    
print("Sum of outputs:", result)


# # 12) A list of words given.Find the words from the list that have their second character in upper case
# 

# In[ ]:


#12) A list of words given.Find the words from the list that have their second character in upper case


# In[29]:


ls=['hello','Dear','hOw','ARe','You']
list=[]
for word in ls:
    if len(word)>=3 and word[1].isupper():
        list.append(word)
print(list)



# # 13 

# In[7]:


# 1)Weight of people in kg
WeightOnEarth = {'John': 45, 'Shelly': 65, 'Marry': 35}

# 2)Gravitational force on the Moon: 1.622 m/s^2
GMoon = 1.622

# 3)Gravitational force on the Earth: 9.81 m/s^2
GEarth = 9.81

# Calculate weight on the Moon for each member
WeightOnMoon = list(map(lambda member: (member[0], (member[1] * GMoon) / GEarth), WeightOnEarth.items()))

# Print the results
for member, weight_moon in WeightOnMoon:
    print(f"{member}'s weight on the Moon: {weight_moon:.2f} kg")


# # ii) CONTROL STRUCTURES

# In[ ]:


#1)Write a python program to find N prime number



num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            
            flag = True
        
            break

    
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


# # 2) Write the python code that calculates the salary of an employee. Prompt the user to enter basic salary,HRA,TA and DA. Add these components to calculate the gross salary. Also,deduct 10% salary from the gross salary to be paid as tax and display gross minus tax as net salary
# 

# In[9]:


basic_salary = float(input("Enter Basic Salary: "))
hra = float(input("Enter House Rent Allowance (HRA): "))
ta = float(input("Enter Travel Allowance (TA): "))
da = float(input("Enter Dearness Allowance (DA): "))

# Calculate the gross salary
gross_salary = basic_salary + hra + ta + da

# Calculate the tax amount (10% of gross salary)
tax = 0.10 * gross_salary

# Calculate the net salary
net_salary = gross_salary - tax

# Print the results
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)


# ## 3 Write a python program to search for a string in the given lists

# In[11]:


# Sample list of strings
my_list = ["Kohli", "dhoni", "jaddu", "Raina", "bumrah"]

# Input string to search for
search_string = input("Enter the string to search for: ")

# Initialize a flag to track whether the string was found or not
found = False

# Iterate through the list to search for the string
for item in my_list:
    if search_string.lower() == item.lower():
        found = True
        break

# Check the flag to determine if the string was found or not
if found:
    print(f"'{search_string}' was found in the list.")
else:
    print(f"'{search_string}' was not found in the list.")


# # 4) Write a python program that accepts a string and calculates no of upper case letters and lower case letters

# In[4]:


def count_case_letters(input_string):
    upper_count = 0
    lower_count = 0
    
    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    return upper_count, lower_count
input_string = "Ronaldo is the Best Footballer in the world"
upper, lower = count_case_letters(input_str)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)


# # 5) Write a program to display the sum of odd numbers and even numbers fall between 12 and 37

# In[7]:


odd_number = 0
even_number = 0

for num in range(12,37):
    
    if num % 2 == 0:
        
        even_number += num
    else:
        odd_number += num
        
print("Sum of even numbers:",even_number)
print("Sum of odd numbers:",odd_number)
        
    


# # 6)program to print table of any number

# In[8]:


number = int(input ("Enter the number: "))
print ("The Multiplication table of: ", number)
for count in range(1, 10):
    print (number, 'x', count, '=', number * count)


# # 7) python program to sum first 10 prime number

# In[1]:


last_number = int(input("\n Please enter the last number  which sum of prime number is to be found:"))
print (" find the sum of prime numbers in p", last_number)
sum = 0

for number in range(2, last_number + 1):

    i = 2
    for i in range(2, number):
        if (int(number % i) == 0):
            i = number
            break;

    if i is not number:
        sum = sum + number
print("\n The sum of prime numbers from 1 to ", last_number, " is :", sum)


# # 8) Python program to implement arithmetic operation using nested if statement

# In[5]:


choice = int(input("Enter your choice:n")) 
print("Enter two numbers: ") 
num1= int (input())
num2= int(input()) 
if choice == 1: 
    res = num1 + num2
    print("Result = ", res)

if choice == 2: 
    res = num1 - num2 
    print("Result", res)
    

if choice == 3:
    res = num1 * num2 
    print("Result = ", res)

if choice == 4:  
    res = num1 / num2
    print("Result = ", res) 

if choice == 5: 
    exit()

else:
    print("Wrong input")


# # 9) Write a python program to take temperature in celsius and convert to a Farenheit

# In[1]:


celsius = int(input("Enter the Temperature in Celsius : \n"))

fahrenheit = (1.8 * celsius) + 32 

print("Temperature in Fahrenheit :", fahrenheit)


# # 10) Write a python program to find maximum and minimum number in a list without using inbuilt function

# In[17]:


def max_min(data): 
    x = data[0]
    y = data[0] 
    for num in data:
        if num> x:
           y= num 
        elif num< y:
            y = num
            return x,y

print (max_min([20, 10, -15, 30, 5, 42, 14, 28, 80]))


# # 11) Write a program in python to print out the number of seconds in 30-day month 30 days, 24 hrs in a day, 60mins per day, 60 secs in minute

# In[1]:


days = 30
hours = 24
minutes = 60
seconds = 60

seconds_in_30_days = days * hours * minutes* seconds

print(f"There are {seconds_in_30_days} seconds in a 30-day month")


# # 12) Write a program in python to print out the number of seconds in a year

# In[4]:


days=365
hours=24
minutes=60
seconds=60
print("Number of seconds in a year : ",days*hours*minutes*seconds)


# # 13) A high speed train can travel at average speed of 150mph, how long will take a train travelling this speed to travel from London to glasgow which is 414 miles away

# In[3]:


distance = 414 
speed = 150

Time_Hours = distance / speed

# Convert hours to hours and minutes
hours = int(Time_Hours)
minutes = (Time_Hours - hours) * 60

# Print the result
print(f"It will take {hours} hours and {minutes:.2f} minutes to travel from London to Glasgow.")


# # 14) Write a python program defines a variable called days_in_each_school_year and assign 192 to variable. The program should print the total hrs that spend in school from yr 7 to 11,each day you spend 6hrs in school days_in_each_school_year = 192          

# In[11]:


# Define the variable days_in_each_school_year
days_in_each_school_year = 192

years = range(7, 12)

# hours spent in school
total_hours = sum(year * days_in_each_school_year * 6 for year in years)

# Prinr the result
print(f"Total hours spent in school from year 7 to year 11: {total_hours} hours")


# # 15)  If the age of Ram,Sam and Khan are input through keyboard , write a python program to determine eldest and youngest of the three

# In[12]:


ram_age = int(input("Enter Ram's age: "))
sam_age = int(input("Enter Sam's age: "))
khan_age = int(input("Enter Khan's age: "))


if ram_age >= sam_age and ram_age >= khan_age:
    eldest = "Ram"
    if sam_age <= khan_age:
        youngest = "Sam"
    else:
        youngest = "Khan"
elif sam_age >= ram_age and sam_age >= khan_age:
    eldest = "Sam"
    if ram_age <= khan_age:
        youngest = "Ram"
    else:
        youngest = "Khan"
else:
    eldest = "Khan"
    if ram_age <= sam_age:
        youngest = "Ram"
    else:
        youngest = "Sam"

print(f"The eldest among Ram, Sam, and Khan is: {eldest}")
print(f"The youngest among Ram, Sam, and Khan is: {youngest}")


# # 16) Write a python program to rotate a list by right n times with and without slicing techniques

# In[19]:


def list_without_slicing(input_list, n):
    if len(input_list) == 0:
        return input_list
    
    n %= len(input_list)  
    for _ in range(n):
        temp = input_list.pop()
        input_list.insert(0, temp)
    return input_list


list = [1, 2, 3, 4, 5]
n = int(input("Enter the number of times to rotate to the right: "))

rotated_list = rotate_list_without_slicing(list, n)
print("Rotate a  list without slicing technique:", rotated_list)


# # 17) Python program to print pattern

# In[24]:


1)#input no of rows in the pattern

n = int(input("Enter the no of rows: "))

def pattern(n, k):
    if k == 0 or k == n:
        return 1
    return pattern(n-1, k - 1) + pattern(n - 1, k)

for i in range(n):
    for j in range(i + 1):
        print(pattern(i, j), end=" ")
    print()
    


# In[27]:


2) # Pattern program
n = 5

for i in range(n):                            
    
    for j in range(i+1):
        
        print("*", end=' ')
    
    print()
        
        


# In[31]:


3 #Input the number of rows for the pattern
n = int(input("Enter the number of rows: "))


for i in range(1, n + 1):
    print(" " * (n - i), end="")  
    print("* " * i)  # 


# In[32]:


4 # print python 

string = input("Enter a string: ")

for i in range(1, len(string) + 1):
    print(string[:i])

