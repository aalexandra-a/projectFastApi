from pydantic import BaseModel

class TrainSchema(BaseModel):
    first_row: str
    second_row: str

class TrainSchema2 (BaseModel):
    id: int = 1
    name: str = "Sasha"
    famil: str = "Kr"
    age: int = 18