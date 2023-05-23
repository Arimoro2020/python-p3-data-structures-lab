spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_foods_names = [food.get("name") for food in spicy_foods]
    return spicy_foods_names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [ food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
       name = food["name"]
       cuisine = food["cuisine"]
       heat_level = food["heat_level"]
       figure = "🌶" * heat_level
       print(f"{name} ({cuisine}) | Heat Level: {figure}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"]==cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
         name = food["name"]
         cuisine = food["cuisine"]
         heat_level = food["heat_level"]
         figure = "🌶" * heat_level
         if heat_level > 5:
             print(f"{name} ({cuisine}) | Heat Level: {figure}")

def get_average_heat_level(spicy_foods):
    sum = 0
    count = len(spicy_foods)
    for food in spicy_foods:
        sum += food.get("heat_level")
    average_heat = sum // count
    return average_heat

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods = spicy_foods + [spicy_food]
    return spicy_foods
