from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/gerar")
def gerar_numero():
    numero_aleatorio = random.randint(1, 100)
    return {"numero_aleatorio": numero_aleatorio}
