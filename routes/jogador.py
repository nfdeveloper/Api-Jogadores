from fastapi import APIRouter
from config.database import conexao
from models.jogador import Jogador
from schemas.jogador import jogadorEntidade,listaJogadoresEntidade
from bson import ObjectId

jogador_router = APIRouter()

@jogador_router.get("/")
async def inicio():
    return "Bem vindo ao FullStack Farm"

@jogador_router.get("/jogadores")
async def lista_jogadores():
    return listaJogadoresEntidade(conexao.local.jogador.find()) 

# Jogador por ID
@jogador_router.get('/jogadores/{jogador_id}')
def buscar_jogador_id(jogador_id):
    return jogadorEntidade(conexao.local.jogador.find_one(
        { "_id": ObjectId(jogador_id) }
    ))

# Inserindo JOGADOR
@jogador_router.post('/jogadores')
async def cadastra_jogadores(jogador: Jogador):
    conexao.local.jogador.insert_one(dict(jogador))
    return listaJogadoresEntidade(conexao.local.jogador.find())

#Atualiza Jogador
@jogador_router.put('/jogadores/{jogador_id}')
async def atualiza_jogador(jogador_id, jogador:Jogador):
    conexao.local.jogador.find_one_and_update(
        {
            "_id": ObjectId(jogador_id)
        },
        {
            "$set": dict(jogador)
        }
    )
    return jogadorEntidade(
        conexao.local.jogador.find_one(
        {
            '_id': ObjectId(jogador_id)
        }
        )
    )

#Exclusão
@jogador_router.delete('/jogadores/{jogador_id}')
async def exclui_jogador(jogador_id):
    return jogadorEntidade(
    conexao.local.jogador.find_one_and_delete(
        {
        "_id": ObjectId(jogador_id)                
        }
    )
    )

