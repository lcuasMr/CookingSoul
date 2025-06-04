from typing import List, Optional
from utils.types import content_type
class Post:
    def __init__(self, 
                 id: Optional[int] = None, 
                 contentType = None,
                 content: Optional[str] = None):
        self._id = id
        self._type = contentType
        self._content = content

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def content(self) -> Optional[str]:
        return self._content

    @content.setter
    def content(self, value: str) -> None:
        self._content = value


    def __str__(self):
        return f"Post({self.id}, {self.content})"
    