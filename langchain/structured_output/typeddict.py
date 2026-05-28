from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str

new_person: Person = {
    "name": "John Doe",
    "age": 30,
    "email": "Johndreckofeler@gmail.com"
}

print(new_person)