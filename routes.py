from fastapi import APIRouter
from random import randint
from schems import TrainSchema
from schems import TrainSchema2
from bzd import f, get_f

api_router = APIRouter()

@api_router.get("/hello")
def hello():
    return {"name" : "Sasha"}

@api_router.get("/rand")
def el():
    return {"num": randint(1, 100)}

#куда данные отправляются гет когда отправляются формат джейсон
@api_router.post("/skey")
def skay(input_data: TrainSchema): #схема данных нам приходит 2 строки
    first_row = input_data.first_row #инициализирует 1 строку
    second_row = input_data.second_row #инициализирует 2 строку
    return {"str" : f"{first_row}{second_row}"}

@api_router.post("/name")
def namee(input_data: TrainSchema2):
    id = input_data.id
    name = input_data.name
    famil = input_data.famil
    age = input_data.age
    f(id, name, famil, age)
    return {
        "id" : id,
        "name" : name,
        "famil" : famil,
        "age" : age
    }

@api_router.get("/get_all")
def get_all():
    return get_f()