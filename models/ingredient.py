from typing import Optional

class Ingredient:
    def __init__(
        self,
        id: Optional[int] = None,
        name: Optional[str] = None,
        region: Optional[str] = None,
        variety: Optional[str] = None,
        flavor: Optional[str] = None,
        medition: Optional[str] = None, # Tipo de medicion aplicada ( ml, l , g, kg, etc )

    ):
        self._id: Optional[int] = id
        self._name: Optional[str] = name
        self._region: Optional[str] = region
        self._variety: Optional[str] = variety
        self._flavor: Optional[str] = flavor
        self._medition: Optional[str] = medition

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def name(self) -> Optional[str]:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def region(self) -> Optional[str]:
        return self._region
    @region.setter
    def region(self, value: str) -> None:
        self._region = value

    @property
    def variety(self) -> Optional[str]:
        return self._variety
    @variety.setter
    def variety(self, value: str) -> None:
        self._variety = value

    @property
    def flavor(self) -> Optional[str]:
        return self._flavor
    @flavor.setter
    def flavor(self, value: str) -> None:
        self._flavor = value

    @property
    def medition(self) -> Optional[str]:
        return self._medition
    @medition.setter
    def medition(self, value: str) -> None:
        self._medition = value

    def __str__(self):
        return f"Ingredient({self.id}, {self.name}, {self.quantity})"