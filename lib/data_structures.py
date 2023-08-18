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
    spicy_names = ([food["name"] for food in spicy_foods])
    print(spicy_names)
    return spicy_names

get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
    spiciest = ([food for food in spicy_foods if food["heat_level"] > 5])
    print(spiciest)
    return(spiciest)

get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    by_cuisine = ([food for food in spicy_foods if food["cuisine"] == cuisine])
    print(by_cuisine)
    return by_cuisine

get_spicy_food_by_cuisine(spicy_foods, "Thai")

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    avg = sum([food["heat_level"] for food in spicy_foods]) / len(spicy_foods)
    print(avg)
    return(avg)

get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

