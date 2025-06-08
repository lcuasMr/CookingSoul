from typing import List, Optional
from utils.types import content_types
class Post:
    def __init__(self, 
                 id: Optional[int] = None, 
                 user_id: Optional[int] = None,
                 content_type = None,
                 description: Optional[str] = None,
                 recipie_id: Optional[int] = None,
                 likes: Optional[int] = 0):
        self._id = id
        self._user = user_id
        self._type = content_type
        self._description = description
        self._recipie_id: Optional[int] = recipie_id
        self._likes: Optional[int] = likes

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def description(self) -> Optional[str]:
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        self._description = value

    @property
    def user_id(self) -> Optional[int]:
        return self._user
    
    @user_id.setter
    def user_id(self, value: int) -> None:
        self._user = value

    @property
    def content_type(self) -> content_types:
        return self._type
    @content_type.setter
    def content_type(self, value: content_type) -> None:
        self._type = value

    @property
    def recipie_id(self) -> Optional[int]:
        return self._recipie_id
    @recipie_id.setter
    def recipie_id(self, value: int) -> None:
        self._recipie_id = value if value is not None else 0

    @property  
    def likes(self) -> Optional[int]:
        return self._likes
    
    @likes.setter
    def likes(self, value: int) -> None:
        self._likes = value if value is not None else 0

    def __str__(self):
        return f"Post({self.id}, {self.description})"
    