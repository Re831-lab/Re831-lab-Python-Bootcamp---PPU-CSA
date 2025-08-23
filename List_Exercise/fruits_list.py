fruits = ["Apple", "Banana", "Orange", "Strawberry", "Grapes"]

print("List of fruits:", fruits)

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

fruits[1] = "Mango"
print("After changing second fruit:", fruits)

fruits.insert(2, "Watermelon")
print("After inserting Watermelon:", fruits)

fruit_name = input("Enter a fruit name: ")
if fruit_name in fruits:
    print(f"{fruit_name} is in the list!")
else:
    print(f"{fruit_name} is NOT in the list.")

fruits.sort()
print("Sorted fruits:", fruits)
