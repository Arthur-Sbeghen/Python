import random

from fastapi import FastAPI, HTTPException, Query

from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Olá Mundo!"}

@app.get("/random-between/")
def get_number(
        min_value: Annotated[int, Query(title="Valor mínimo", ge=1, le=1000)] = 1,
        max_value: Annotated[int, Query(title="Valor máximo", ge=1, le=1000)] = 1000
    ):
    if min_value >= max_value:
        raise HTTPException(status_code=400, detail="O valor mínimo deve ser menor que o valor máximo.")
    
    return {
        "min": min_value,
        "max": max_value,
        "random": random.randint(min_value, max_value)
    }

db = []

@app.post("/items")
def add_item(body: dict):
      item_name = body.get("name")
      if not item_name:
          raise HTTPException(status_code=400, detail="O campo 'nome' é obrigatório")

      if item_name in items_db:
          raise HTTPException(status_code=400, detail="O item já existe")

      items_db.append(item_name)
      return {"message": "O item foi adicionado com sucesso", "item": item_name}

@app.get("/items")
def get_items():
    return {"items": db}

@app.put("/items/{item}")
def update_item(name: str, body: dict):
    if name not in db:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    
    new_name = body.get('name')

    if not new_name:
        raise HTTPException(status_code=400, detail="O campo 'nome' é obrigatório")
    
    if new_name in db:
        raise HTTPException(status_code=400, detail="O item já existe")
    
    index = db.index(name)
    db[index] = new_name

    return {
        "status": 200,
        "message": f"O item {name} foi atualizado para {new_name}"
    }

@app.delete("/items/{item}")
def delete_item(item: str):
    if name not in db:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    
    db.remove(item)

    return {
        "status": 200,
        "message": f"O item {item} foi removido com sucesso"
    }