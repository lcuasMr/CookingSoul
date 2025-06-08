from typing import List, Optional

from models.post import Post

class User:
    def __init__(self, 
                 id: Optional[int] = None, 
                 username: Optional[str] = None, 
                 email: Optional[str] = None,
                 password: Optional[str] = None,
                 posts: Optional[list[Post]] = None):
        self._id = id
        self._username = username
        self._email = email
        self._password = password
        self._posts = posts

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def username(self) -> Optional[str]:
        return self._username

    @username.setter
    def username(self, value: str) -> None:
        self._username = value

    @property
    def email(self) -> Optional[str]:
        return self._email
    
    @email.setter
    def email(self, value: str) -> None:
        self._email = value

    @property
    def password(self) -> Optional[str]:
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        self._password = value

    @property
    def posts(self) -> Optional[list[Post]]:
        return self._posts

    @posts.setter
    def posts(self, value: list[Post]) -> None:
        self._posts = value


    def __str__(self):
        return f"Usuario({self.id}, {self.username}, {self.password})"
    