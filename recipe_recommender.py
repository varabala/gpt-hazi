import pymongo
import re
import requests


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["recept_ajanlo"]  # Adatbázis neve
collection = db["receptek"]  # Kollekció neve


if collection.count_documents({}) == 0:
    url = "https://raw.githubusercontent.com/varabala/gpt-hazi/main/receptek.md"
    response = requests.get(url)
    recipes_md = response.text

    recipe_pattern = re.compile(r"## (.+)\n(.+)\n- Típus: (.+)\n- Konyha: (.+)\n- Elkészítési idő: (.+) perc")
    for match in recipe_pattern.finditer(recipes_md):
        recipe = {
            "name": match.group(1),
            "ingredients": [ingredient.strip() for ingredient in match.group(2).split(",")],
            "type": match.group(3),
            "cuisine": match.group(4),
            "prep_time": int(match.group(5)),
        }
        collection.insert_one(recipe)


recipes = list(collection.find())

def get_user_preferences():
    preferences = {}
    preferences["liked_ingredients"] = input("Milyen összetevőket szeretsz? (vesszővel elválasztva): ").split(",")
    preferences["disliked_ingredients"] = input("Milyen összetevőket NEM szeretsz? (vesszővel elválasztva): ").split(",")
    preferences["liked_types"] = input("Milyen étel típusokat szeretsz? (vesszővel elválasztva): ").split(",")
    preferences["liked_cuisines"] = input("Milyen konyhákat szeretsz? (vesszővel elválasztva): ").split(",")
    return preferences

def filter_recipes(recipes, preferences):
    filtered_recipes = []
    for recipe in recipes:
        if not any(ingredient in recipe["ingredients"] for ingredient in preferences["disliked_ingredients"]) and \
           any(recipe_type in recipe["type"] for recipe_type in preferences["liked_types"]):
            filtered_recipes.append(recipe)
    return filtered_recipes

def rank_recipes(recipes, preferences):
    for recipe in recipes:
        score = 0
        if any(ingredient in recipe["ingredients"] for ingredient in preferences["liked_ingredients"]):
            score += 1
        if any(cuisine in recipe["cuisine"] for cuisine in preferences["liked_cuisines"]):
            score += 1
        recipe["score"] = score
    return sorted(recipes, key=lambda recipe: recipe["score"], reverse=True)

def recommend_recipes(preferences):
    filtered_recipes = filter_recipes(recipes, preferences)
    ranked_recipes = rank_recipes(filtered_recipes, preferences)
    for recipe in ranked_recipes[:3]:
        print(f"- {recipe['name']} ({recipe['type']}, {recipe['cuisine']})")
