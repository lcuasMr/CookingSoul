from models.ingredient import Ingredient

class IngredientMapper:
    @staticmethod
    def map(json_data):
        id = json_data.get('id')
        name = json_data.get('name')
        region = json_data.get('region')
        variety = json_data.get('variety')
        flavor = json_data.get('flavor')
        medition = json_data.get('medition')
        return Ingredient(id, name, region, variety, flavor, medition)

    @staticmethod
    def reverse_map(ingredient):
        return {
            'id': ingredient.id,
            'name': ingredient.name,
            'region': ingredient.region,
            'variety': ingredient.variety,
            'flavor': ingredient.flavor,
            'medition': ingredient.medition
        }