from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: Optional[int]
    first_name: str
    last_name: str
    email: str
    password: str
    ssn: str
