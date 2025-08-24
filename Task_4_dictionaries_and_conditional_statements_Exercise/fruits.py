fruit_prices = {
    "apple": 2.5,
    "banana": 1.2,
    "orange": 1.8,
    "mango": 3.0,
    "grapes": 2.0
}

fruit = input("Enter the name of a fruit: ").lower()

if fruit in fruit_prices:
    print("The price of", fruit, "is", fruit_prices[fruit])
else:
    print("Sorry, this fruit is not available.")
