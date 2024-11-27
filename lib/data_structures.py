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
    foods = list()
    for food in spicy_foods:
        foods.append(food["name"])
    return foods
    pass

def get_spiciest_foods(spicy_foods):
    foods = list()
    for food in spicy_foods:
        if food["heat_level"] > 5:
            foods.append(food)
    return foods
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        level = food["heat_level"] * '🌶'
        print(f"{name} ({cuisine}) | Heat Level: {level}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            level = food["heat_level"] * '🌶'
            print(f"{name} ({cuisine}) | Heat Level: {level}")
    pass

def get_average_heat_level(spicy_foods):
    foods = list()
    for food in spicy_foods:
        foods.append(food["heat_level"])
    avg = sum(foods) / len(foods)
    return avg
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
