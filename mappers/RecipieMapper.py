from models.recipie import Recipie

from mappers.IngredientMapper import IngredientMapper

import sys

class RecipieMapper:
    @staticmethod
    def map(json_data):
        ingredientmapper = IngredientMapper()
        id = json_data.get('id')
        title = json_data.get('title')
        description = json_data.get('description')
        ingredients = [ingredientmapper.map(ingredient) for ingredient in json_data.get('ingredients', [])]
        instructions = json_data.get('instructions')
        return Recipie(id, title, description, ingredients, instructions)

    @staticmethod
    def reverse_map(recipie: Recipie):
        ingredientmapper = IngredientMapper()
        print(recipie, file=sys.stdout)
        return {
            'id': recipie.id,
            'title': recipie.title,
            'description': recipie.description,
            'ingredients': recipie.ingredients,
            'instructions': recipie.instructions
        }