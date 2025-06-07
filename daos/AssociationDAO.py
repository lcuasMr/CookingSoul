from sqlalchemy.orm import Session
from entities.association_tables import RecipieIngredientAssociation

class AssociationDAO:
    def __init__(self, session: Session):
        self.session = session

    def add_association(self, recipie_id: int, ingredient_id: int, cuantity: int):
        association = RecipieIngredientAssociation(
            recipie_id=recipie_id,
            ingredient_id=ingredient_id,
            cuantity=cuantity
        )
        self.session.add(association)
        self.session.commit()
        return association

    def get_associations_by_recipie(self, recipie_id: int):
        return self.session.query(RecipieIngredientAssociation).filter_by(recipie_id=recipie_id).all()

    def get_associations_by_ingredient(self, ingredient_id: int):
        return self.session.query(RecipieIngredientAssociation).filter_by(ingredient_id=ingredient_id).all()

    def delete_association(self, recipie_id: int, ingredient_id: int):
        association = self.session.query(RecipieIngredientAssociation).filter_by(
            recipie_id=recipie_id,
            ingredient_id=ingredient_id
        ).first()
        if association:
            self.session.delete(association)
            self.session.commit()
            return True
        return False