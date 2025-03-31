from fastapi import FastAPI

app = FastAPI()

# inicial no fastapi
@app.get('/')
async def root():
    return{'message':'Hello World'}

crepusculo_idade = {
    1: {"Nome": "Edward Cullen", "idade": 104}, 
    2: {"Nome": "Isabella Swanaria", "idade": 18},
    3: {"Nome": "Jacob Black", "idade": 16},
    4: {"Nome": "Renesmee Cullen", "idade": 4}, 
    5: {"Nome": "Alice Cullen", "idade": 104},
    6: {"Nome": "Jasper Hale", "idade": 120},
    7: {"Nome": "Rosalie Hale", "idade": 90},
    8: {"Nome": "Esme Cullen", "idade": 100},
    9: {"Nome": "Emmett Cullen", "idade": 105},
    10: {"Nome": "Charlie Swan", "idade": 40}
}

@app.get("/personagem/{item_id}")
async def read_item(item_id: int):
    chaves = crepusculo_idade.keys()
    print(chaves)
    if item_id not in chaves:
        return {"mensagem": "Idade e personagem não encontrado"}
    return f"Personagem: {crepusculo_idade[item_id]}"

# exemplo de quest parameters
crepusculo_personagens = {
    1 : {"personagem": "Edward Cullen",     "ator": "Robert Pattinson"},
    2 : {"personagem": "Isabella Swan",     "ator": "Kristen Stewart"},
    3 : {"personagem": "Jacob Black",       "ator": "Taylor Lautner"},
    4 : {"personagem": "Renesmee Cullen",   "ator": "Mackenzie Foy"},
    5 : {"personagem": "Alice Cullen",      "ator": "Ashley Greene"},
    6 : {"personagem": "Jasper Hale",       "ator": "Jackson Rathbone"},
    7 : {"personagem": "Rosalie Hale",      "ator": "Nikki Reed"},
    8 : {"personagem": "Esme Cullen",       "ator": "Elizabeth Reaser"},
    9 : {"personagem": "Emmett Cullen",     "ator": "Kellan Lutz"},
    10 : {"personagem": "Charlie Swan",      "ator": "Billy Byrke"}
}


@app.get("/todos-atores/{item_id}")
async def read_item(item_id: int):
    chaves = crepusculo_personagens.keys()
    print(chaves)
    if item_id not in chaves:
        return {"mensagem": "Peronagem e ator não encontrado"}
    return f"Ator: {crepusculo_personagens[item_id]}"
