from fastapi import APIRouter
from config.database import conexao
from models.jogador import Jogador
from schemas.jogador import jogadorEntidade,listaJogadoresEntidade

jogador_router = APIRouter()

@jogador_router.get("/")
async def inicio():
    return "Bem vindo ao FullStack Farm"

@jogador_router.get("/jogadores")
async def lista_jogadores():
    return listaJogadoresEntidade(conexao.local.jogador.find()) 

# Inserindo JOGADOR
@jogador_router.post('/jogadores')
async def cadastra_jogadores(jogador: Jogador):
    conexao.local.jogador.insert_one(dict(jogador))
    return listaJogadoresEntidade(conexao.local.jogador.find())
