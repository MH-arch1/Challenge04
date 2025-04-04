fruits = ("apple", "banana", "cherry", "apple", "banana","cherry", "apple", "banana", "orange" , "blueberry")
user_fruits = input("Enter your favourite fruit: ").lower().strip()
total_fruits = fruits.count(user_fruits)
print("your fruit appears", total_fruits, "times in the tuple")