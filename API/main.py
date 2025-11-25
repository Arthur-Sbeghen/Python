import random
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

class Nota(BaseModel):
    name: str
    data: str = None  # Campo opcional para data

@app.post("/notas")
def add_item(nota: Nota):
    if not nota.name:
        raise HTTPException(status_code=400, detail="O campo 'nome' é obrigatório")

    if nota.name in db:
        raise HTTPException(status_code=400, detail="O item já existe")

    db.append(nota.name)
    return {"message": "O item foi adicionado com sucesso", "item": nota.name}

@app.get("/notas")
def get_items():
    return {"items": db}

@app.put("/notas/{name}")
def update_item(name: str, nota: Nota):
    if name not in db:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    
    if not nota.name:
        raise HTTPException(status_code=400, detail="O campo 'nome' é obrigatório")
    
    if nota.name in db and nota.name != name:
        raise HTTPException(status_code=400, detail="O item já existe")
    
    index = db.index(name)
    db[index] = nota.name

    return {
        "message": f"O item {name} foi atualizado para {nota.name}"
    }

@app.delete("/notas/{item}")
def delete_item(item: str):
    if item not in db:  # CORREÇÃO: mudado de 'name' para 'item'
        raise HTTPException(status_code=404, detail="Item não encontrado")
    
    db.remove(item)

    return {
        "message": f"O item {item} foi removido com sucesso"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)