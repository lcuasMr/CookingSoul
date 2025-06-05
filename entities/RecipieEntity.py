from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import mapped_column, relationship, Mapped
from sqlalchemy.ext.declarative import declarative_base
from models.recipie import Recipie
from models.ingredient import Ingredient
from models.RecetaIngrediente import RecetaIngrediente

Base = declarative_base()

class RecipieEntity(Base):
    __tablename__ = 'recipie'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    title = mapped_column(String(200), nullable=False)
    description = mapped_column(Text, nullable=True)
    ingredientes_asociados = relationship(
        "IngredientEntity",
        secondary='receta_ingrediente',
        back_populates="recetas_asociadas"
    )
    instructions = mapped_column(Text, nullable=True)

    def __init__(self, recipie_model):
        super().__init__()
        self.id = recipie_model.id
        self.title = recipie_model.title
        self.description = recipie_model.description
        self.ingredientes = recipie_model.ingredient
        self.instructions = recipie_model.instructions

    def __repr__(self):
        return (
            f"<RecipieEntity(id={self.id}, title='{self.title}', description='{self.description}', "
        )

    def to_model(self) -> Recipie:
        ingredients_list = [
            RecetaIngrediente(
                ingrediente=ri.ingrediente.to_model(),
                cantidad=ri.cantidad,
                unidad=ri.unidad
            )
            for ri in self.ingredientes_asociados
        ]
        
        return Recipie(
            id=self.id,
            title=self.title,
            description=self.description,
            ingredient=ingredients_list,
            instructions=self.instructions
        )