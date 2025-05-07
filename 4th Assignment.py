#Q1.

#An e-commerce store stores information about its products in a nested dictionary. 
#The outer dictionary uses product IDs as keys, and the inner dictionary stores 
#product details like name, category, price, and stock quantity. 
products = { 101: {"name": "Laptop", "category": "Electronics", "price": 1200, "stock": 50}, 
102: {"name": "Shirt", "category": "Apparel", "price": 25, "stock": 200}, 103: 
{"name": "Coffee Maker", "category": "Home Appliances", "price": 80, "stock": 30} }

#• Increase the stock of the "Shirt" product (add 50 more units)



products[102] ["stock"] += 500
print(products)
#• Add a new product (e.g., "Smartphone")

products [104] = {"name": "Smartphone"}

#Q2.You are given a list that contains some duplicate items. Remove the duplcates
shopping_list = ["apple", "banana", "apple", "orange", "banana", "grape"]
a= list(set(shopping_list))
print(a)



#Q3.You are managing a list of students enrolled in two different courses. You need to perform various set operations to understand the student enrollment. Task: Create two sets: one for students in "Course A" and one for students in "Course B". Find the students who are in "Course A" but not in "Course B" (difference). Find students who are only in one of the two courses (symmetric difference). 

course_a = {"John", "Alice", "Bob", "David"} 

course_b = {"Alice", "Eve", "Charlie", "David"}

#• Find students who are in Course A but not in Course B (difference)

#• Find students who are only in one of the two courses (symmetric difference)

a = course_a - course_b
print(a)
b = course_a^course_b
print(b)



#Q4.
#Write a Python program that calculates the sum of all even numbers between 1 and 50 (inclusive) using a for loop.

c = 0
for i in range(1,51):
    if i %2 ==0:
        c +=i
print(c)



#Q5. Power of a Number Write a Python program that takes a number and prints the powers of the number (starting from 1 to 10) using a while loop. For example, if the user inputs 3, the output should be:


inp = int(input ("Pls enter your number : "))
c = 1
while c <11:
   a = inp **c
   c+=1
print(a)


#Q6 Problem Statement: Write a Python program that takes an integer input from the user and counts down from that number to 0. The program should display the current number at each step until it reaches 0, at which point it should print a message indicating the countdown is finished

a = int(input("Pls enter your number : "))
while a > 0: 
    print(a)  
    a -= 1  


#Q7 Write a Python program that takes a number as input from the user and calculates its factorial using a for loop. The program should display the result to the user.

fac = int(input("Pls enter yoru number : "))
print(fac*fac)


#Q8 Create an empty dictionary called person_info.
#Assign the following key-value pairs to the dictionary:

dic = {"name " : "Alice" , "age" : "23" , "occupation" : "Engineer"}
print(dic)


#Q9 Printing a right-angled triangle pattern (with NESTED while loop)

n = int(input("Enter the number of rows for the triangle: "))

i = 1  
while i <= n:
    j = 1 
    while j <= i:
        print("*", end="")  
        j += 1
    print()  
    i += 1  

#Q10 Write a Python program that does the following:

# Range: Loop through numbers from 1 to 20 (inclusive).

# Continue: If the number is divisible by 4, skip that iteration and move to the next number.

# Break: If the number is divisible by 7, stop the loop entirely.

# For all other numbers, print the number.



for i in range(1,21):
    if i %4 == 0:
        continue
    if i % 7 ==0:
        break
print(  i)

