# #Question 1: Age Group Classification 
# #Write a Python program that takes the age of a person as input and classifies them into one of the following age groups:

age = int(input("Pls enter your age : "))
if age <=12:
    print("Child")
elif age >=13 and age <=19:
    print("Teenager")
elif age >=20 and age <=64:
    print("Adult")

else:
    print("Senior")

#Q2. Write a Python program that asks the user to enter an email address. The program should check if the email contains the characters @ and "." (ignoring case). If either character is present, print "Email format is valid." Otherwise, print "Invalid email format."

email = input("Enter your mail : ")
print("Email format is valid" if "@" in email and "." in email else("Invalid email format."))

#Q3. Write a Python program that takes three numbers as input and determines the largest among them. Also, check if any or all of the numbers are equal."

num1 = int(input("Enter 1st number1 : "))
num2 = int(input("Enter 2nd number2 : "))
num3 = int(input("Enter 3rd number3 : "))

if num1 >=num2 and num1>=num3:
    print("The largest num is ", num1)

elif num2>=num1 and num2>=num3:
    print("Largest num is " ,num2)

elif num1 == num2 and num1 ==num3 :
    print("All number of same")


else: print("Largest number is ",num3)


#Q4. Write a Python program that:

num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("The number is positive and even")
    else:
        print("The number is positive and odd")
else:
    print("The number is not positive")




# #Q5. Ask the user for a username and password. Check if the username is correct. If it is, then check if the password is correct. If both are correct, print "Access granted".

userman = input("Pls enter your ID : ")
pass1 = input("Pls enter your password : ")

if userman == "admin" and pass1 == "1234":
    print("Access Grande")

else: print ("User or Password is incorrect")



#Q6. Take an integer input from the user and 
#check whether the entered value exists in the tuple my_tuple = (5, 10, 15, 20, 25). Print an appropriate message based on the result.
my_tuple = (5, 10, 15, 20, 25)
a = int(input("Pls pass one int : "))
if a in my_tuple:
    print("This int is exixt")
else: print("Not exixt")

#Q7. Create a program that takes the user's first name, last name, and age as input, packs them into a tuple, and prints the tuple.

fname = str(input("Pls enter yoru name : "))
lname = str(input("Pls enter lname : "))
age = int(input("Enter your age : "))

b= ( fname , lname , age)
print(b)

#Q8. Given the tuple coordinates = (4, 5, 6), unpack the elements of the tuple into three variables x, y, and z. Then, calculate and print the sum of the variables.

coordinates = (4, 5, 6)
x,y,z = coordinates
print(x+y+z)

#Q9. Given the tuple my_tuple = (1, 2, 3, 4, 5), remove the element 3 from the tuple by first converting it to a list, and then print the resulting tuple.

my_tuple = (1, 2, 3, 4, 5)
temp_list = list(my_tuple)       
temp_list.remove(3)              
new_tuple = tuple(temp_list)     
print(new_tuple)

#Q10. Given the tuple numbers = (10, 20, 5, 30, 15), find and print the maximum and minimum values in the tuple.

numbers = (10, 20, 5, 30, 15)
print(max(numbers))
print(min(numbers))
