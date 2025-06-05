from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapped_column
from sqlalchemy.ext.declarative import declarative_base
from models.ingredient import Ingredient

Base = declarative_base()

class IngredientEntity(Base):
    __tablename__ = 'ingredients'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(100), nullable=False)
    region = mapped_column(String(100), nullable=True)
    variety = mapped_column(String(100), nullable=True)
    flavor = mapped_column(String(100), nullable=True)
    medition = mapped_column(String(50), nullable=True)

    def __init__(self, ingredient_model):
        super().__init__()
        self.id = ingredient_model.id
        self.name = ingredient_model.name
        self.region = ingredient_model.region
        self.variety = ingredient_model.variety
        self.flavor = ingredient_model.flavor
        self.medition = ingredient_model.medition

    def __repr__(self):
        return (
            f"<IngredientEntity(id={self.id}, name='{self.name}', region='{self.region}', "
            f"variety='{self.variety}', flavor='{self.flavor}', medition='{self.medition}')>"
        )

    def to_model(self) -> Ingredient:
        return Ingredient(
            id=self.id,
            name=self.name,
            region=self.region,
            variety=self.variety,
            flavor=self.flavor,
            medition=self.medition
        )