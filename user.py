from dataclasses import dataclass


@dataclass
class user:
    id: int
    username: str
    first_name: str
    last_name: str
    age: int
