from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base
from models.recipie import Recipie
from models.ingredient import Ingredient

Base = declarative_base()

class RecetaIngredienteEntity(Base):
    __tablename__ = 'receta_ingrediente'
    receta_id = mapped_column(Integer, ForeignKey('recipies.id'), primary_key=True)
    ingrediente_id = mapped_column(Integer, ForeignKey('ingredients.id'), primary_key=True)
    cantidad = mapped_column(Float, nullable=False)
    unidad = mapped_column(String(20), nullable=False)

    receta = relationship("RecetaEntity", back_populates="ingredientes_asociados")
    ingrediente = relationship("IngredientEntity", back_populates="recetas_asociadas")

    def __init__(self, receta_id: int, ingrediente_id: int, cantidad: float, unidad: str):
        self.receta_id = receta_id
        self.ingrediente_id = ingrediente_id
        self.cantidad = cantidad
        self.unidad = unidad