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
        image_url = json_data.get('image_url', None)
        return Ingredient(id, name, region, variety, flavor, medition, image_url)

    @staticmethod
    def reverse_map(ingredient):
        return {
            'id': ingredient.id,
            'name': ingredient.name,
            'region': ingredient.region,
            'variety': ingredient.variety,
            'flavor': ingredient.flavor,
            'medition': ingredient.medition,
            'image_url': ingredient.image_url
        }