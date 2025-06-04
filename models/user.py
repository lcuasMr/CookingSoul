from typing import List, Optional

class User:
    def __init__(self, 
                 id: Optional[int] = None, 
                 username: Optional[str] = None, 
                 email: Optional[str] = None,
                 password: Optional[str] = None):
        self._id = id
        self._username = username
        self._email = email
        self._password = password

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


    def __str__(self):
        return f"Usuario({self.id}, {self.nombre}, {self.password})"
    