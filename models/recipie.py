from typing import Optional, List
from models.ingredient import Ingredient
from datetime import datetime

class Recipie:
    def __init__(
        self,
        id: Optional[int] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        ingredients: Optional[tuple] = None,
        instructions: Optional[str] = None
    ):
        self._id: Optional[int] = id
        self._title: Optional[str] = title
        self._description: Optional[str] = description
        self._ingredients: Optional[list[tuple]] = ingredients
        self._instructions: Optional[str] = instructions

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def title(self) -> Optional[str]:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        self._title = value

    @property
    def description(self) -> Optional[str]:
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        self._description = value

    @property
    def ingredients(self) -> Optional[list[tuple]]:
        return self._ingredients

    @ingredients.setter
    def ingredients(self, value: list[tuple]) -> None:
        self._ingredients = value

    @property
    def instructions(self) -> Optional[str]:
        return self._instructions

    @instructions.setter
    def instructions(self, value: str) -> None:
        self._instructions = value

    def __str__(self):
        return (
            f"Recipie({self.id}, {self.title}, {self.description}, "
            f"{self.ingredients}, {self.instructions})"
        )