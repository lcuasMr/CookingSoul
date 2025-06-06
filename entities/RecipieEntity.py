from sqlalchemy import Column, Integer, String, Text, ARRAY
from sqlalchemy.orm import mapped_column, relationship, Mapped
from sqlalchemy.ext.declarative import declarative_base
from models.recipie import Recipie
from daos.IngredientDAO import IngredientDAO
import json
from entities.association_tables import RecipieIngredientAssociation

from entities import Base

import sys

class RecipieEntity(Base):
    __tablename__ = 'recipies'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    title = mapped_column(String(200), nullable=False)
    description = mapped_column(Text, nullable=True)
    instructions = mapped_column(Text, nullable=True)

    ingredients: Mapped[list["RecipieIngredientAssociation"]] = relationship(back_populates="recipie")


    def __init__(self, recipie_model):
        print(f"Creating RecipieEntity with model: {recipie_model}", file=sys.stdout)
        super().__init__()
        self.id = recipie_model.id
        self.title = recipie_model.title
        self.description = recipie_model.description
        self.ingredients = []
        self.instructions = recipie_model.instructions

    def __repr__(self):
        return (
            f"<RecipieEntity(id={self.id}, title='{self.title}', description='{self.description}', "
        )

    def to_model(self) -> Recipie:
        return Recipie(
            id=self.id,
            title=self.title,
            description=self.description,
            instructions=self.instructions
        )