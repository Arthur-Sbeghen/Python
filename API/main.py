import random
import time
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Annotated, Optional
from google import genai

client = genai.Client(api_key="aaa")

def gerar_descricao(titulo: str) -> str:
    prompt = f"""
    Você é um sistema que gera descrições de notas.

    Gere APENAS UMA descrição curta, direta e objetiva para a nota abaixo.
    NÃO gere listas.
    NÃO gere variações.
    NÃO ofereça opções.
    NÃO use aspas.
    NÃO explique nada.

    Título da nota: {titulo}

    Responda apenas com a descrição.
    """
    
    MAX_RETRIES = 5

    for _ in range(MAX_RETRIES):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text.strip()
        except Exception:
            time.sleep(2)

    return "Descrição não pôde ser gerada no momento."


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=False,
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
        raise HTTPException(
            status_code=400,
            detail="O valor mínimo deve ser menor que o valor máximo."
        )
    
    return {
        "min": min_value,
        "max": max_value,
        "random": random.randint(min_value, max_value)
    }


db = []


class Nota(BaseModel):
    name: str
    data: Optional[str] = None


class NotaDB(BaseModel):
    name: str
    data: Optional[str]
    descricao: str


@app.post("/notas")
def add_item(nota: Nota):
    if not nota.name.strip():
        raise HTTPException(status_code=400, detail="O campo 'nome' é obrigatório")

    if any(n["name"] == nota.name for n in db):
        raise HTTPException(status_code=400, detail="O item já existe")

    descricao = gerar_descricao(nota.name)

    nova_nota = {
        "name": nota.name,
        "data": nota.data,
        "descricao": descricao
    }

    db.append(nova_nota)

    return {
        "message": "Nota criada com sucesso",
        "item": nova_nota
    }


@app.get("/notas")
def get_items():
    return {"items": db}


@app.put("/notas/{name}")
def update_item(name: str, nota: Nota):
    for item in db:
        if item["name"] == name:
            item["name"] = nota.name
            item["data"] = nota.data
            item["descricao"] = gerar_descricao(nota.name)
            return {"message": "Nota atualizada com sucesso", "item": item}

    raise HTTPException(status_code=404, detail="Item não encontrado")


@app.delete("/notas/{name}")
def delete_item(name: str):
    for item in db:
        if item["name"] == name:
            db.remove(item)
            return {"message": "Nota removida com sucesso"}

    raise HTTPException(status_code=404, detail="Item não encontrado")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
