from typing import Optional
from models.ingredient import Ingredient
from models.recipie import Recipie

class RecetaIngrediente:
    def __init__(
        self,
        receta: Optional[Recipie] = None,
        ingrediente: Optional[Ingredient] = None,
        cantidad: Optional[str] = None,
        unidad: Optional[str] = None
    ):
        self._receta: Optional[Recipie] = receta
        self._ingrediente: Optional[Ingredient] = ingrediente
        self._cantidad: Optional[str] = cantidad
        self._unidad: Optional[str] = unidad

    @property
    def receta(self) -> Optional[Recipie]:
        return self._receta

    @receta.setter
    def receta(self, value: Recipie) -> None:
        self._receta = value

    @property
    def ingrediente(self) -> Optional[Ingredient]:
        return self._ingrediente

    @ingrediente.setter
    def ingrediente(self, value: Ingredient) -> None:
        self._ingrediente = value

    @property
    def cantidad(self) -> Optional[str]:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, value: str) -> None:
        self._cantidad = value

    @property
    def unidad(self) -> Optional[str]:
        return self._unidad

    @unidad.setter
    def unidad(self, value: str) -> None:
        self._unidad = value

    def __str__(self):
        return f"{self.cantidad} {self.unidad or ''} de {self.ingrediente} en {self.receta}"