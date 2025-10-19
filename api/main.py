# importando a biblioteca
from fastapi import FastAPI, HTTPException, status
from typing import Optional
from model import Filme

# chamando a método do fast
app = FastAPI(title='API Filmes Studios Ghibli')

# inserindo os dados manualmente mas seguindo a base estabelecida em models.py
filmes = {
    1:{
        "titulo" : "Meu Vizinho Totoro",
        "ano_lancamento" : 1988,
        "diretor" : "Hayao Miyazaki"
    },
    2:{
        "titulo" : "Serviço de Entrega da Kiki",
        "ano_lancamento" : 1989,
        "diretor" : "Hayao Miyazaki"
    },
    3:{
        "titulo" : "A Viagem de Chihiro",
        "ano_lancamento" : 2001,
        "diretor" : "Hayao Miyazaki"
    },
    4:{
        "titulo" : "O Castelo Animado",
        "ano_lancamento" : 2004,
        "diretor" : "Hayao Miyazaki"
    },
    5:{
        "titulo" : "Ponyo",
        "ano_lancamento" : 2008,
        "diretor" : "Hayao Miyazaki"
    },
    6:{
        "titulo" : "O Menino e a Garça",
        "ano_lancamento" : 2023,
        "diretor" : "Hayao Miyazaki"
    }
}


@app.get("/filmes", summary='Retorna todos os Filmes')
async def get_filmes():
    return filmes


@app.get("/filmes/{filme_id}", summary='Retorna o filme pelo id')
async def get_filme(filme_id:int):
    # usando o try/except para controle de erros
    try:
        filme = filmes[filme_id]
        return filme
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Filme Não Encontrado ಥ_ಥ')
    


@app.post("/filmes", status_code=status.HTTP_201_CREATED, summary='Públicar Novo Filme')
async def post_filme(filme: Optional[Filme] = None):

    # essa parte serve para o id não se repetir e sempre ser crescente
    next_id = len(filmes) + 1
    filmes[next_id] = filme
    del filme.id
    return filme


# para editar individualmente cada filme
@app.put('/filmes/{filme_id}', summary='Editar o filme pelo id')
async def put_filme(filme_id: int, filme: Filme):
    # se o id digitado estiver entre a lista criada de filmes então libera para editar
    if filme_id in filmes:
        filmes[filme_id] = filme
        filme.id = filme_id
        return filme
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Filme Não Encontrado ಥ_ಥ")

@app.delete('/filmes/{filme_id}', summary='Excluir o filme pelo id')
async def delete_filme(filme_id: int):
    if filme_id in filmes:
        del filmes[filme_id]
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Filme Não Encontrado ಥ_ಥ")



# configs para executar o server com o uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)