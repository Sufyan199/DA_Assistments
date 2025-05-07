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



