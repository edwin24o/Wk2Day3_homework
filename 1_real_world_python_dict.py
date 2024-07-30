# Task 1: Restaurant Menu Update
# You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update this menu based on given instructions. This exercise tests your ability to manipulate nested dictionaries and manage data effectively.

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Soda": 2.99, "Margartita": 3.99}  #Add a new category called "Beverages" with at least two items.
print(restaurant_menu)

restaurant_menu["Main Course"]["Steak"] = 17.99  #Update the price of "Steak" to 17.99.
print(restaurant_menu)

del restaurant_menu["Starters"]["Bruschetta"]  #Remove "Bruschetta" from "Starters".
print(restaurant_menu)