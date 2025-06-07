# entities/association_tables.py

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped



from entities import Base


class RecipieIngredientAssociation(Base):
    __tablename__ = 'recipie_ingredient_association'

    recipie_id = mapped_column( ForeignKey('recipies.id'), primary_key=True)
    ingredient_id = mapped_column( ForeignKey('ingredients.id'), primary_key=True)
    cuantity = mapped_column(Integer, nullable=False)

    ingredient: Mapped["IngredientEntity"] = relationship(back_populates="recipies")
    recipie: Mapped["RecipieEntity"] = relationship(back_populates="ingredients")

    def __init__(self, recipie_id: int, ingredient_id: int, cuantity: int = 1):
        self.recipie_id = recipie_id
        self.ingredient_id = ingredient_id
        self.cuantity = cuantity

    def __repr__(self):
        return f"<RecipieIngredientAssociation(recipie_id={self.recipie_id}, ingredient_id={self.ingredient_id}, cuantity={self.cuantity})>"
