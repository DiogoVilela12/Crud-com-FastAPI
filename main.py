from fastapi import FastAPI
from typing import Optional
from Utils import validação
from Utils import arquivo
import sqlite3

app = FastAPI()
banco_de_dados = 'Banco De Dados/bancodedados.txt'


@app.get("/")
async def root():
    return {'Bem Vindo !!!'}


@app.get("/cadastro")
async def cadastro(nome: str, cpf: int, idade: int):
    conn = sqlite3.connect('Banco De Dados/banco_de_dados.db')
    cursor = conn.cursor()

    # Fazendo cadastro do usuario
    print(nome, idade, cpf)
    cursor.execute(f"""
    INSERT INTO User (nome, idade, cpf)
    VALUES ('{nome}', {idade}, '{cpf}')""")

    conn.commit()
    conn.close()
    return {f'Cadastro do(a) {nome} Realizado com sucesso !!!'}


@app.get("/banco de dados")
async def acessar_bd():
    conn = sqlite3.connect('Banco De Dados/banco_de_dados.db')
    cursor = conn.cursor()
    dados = []

    # Leitura dos dados da DB
    cursor.execute("""
    SELECT * FROM User;
    """)

    for linha in cursor.fetchall():
        print(linha)
        dados.append(linha)
    conn.close()
    return dados


@app.get("/modificar usuario")
async def modificar_usuario(id_atual: int, nome: Optional[str], cpf: Optional[int], idade: Optional[int]):
    conn = sqlite3.connect('Banco De Dados/banco_de_dados.db')
    cursor = conn.cursor()

    # Alterando dados de um usuario
    cursor.execute(f"""
    UPDATE User
    SET nome = '{nome}', cpf = '{cpf}', idade = {idade}
    WHERE id = {id_atual}""")

    conn.commit()
    conn.close()

    return {f'Dados do Usuario(a): {nome} atualizados com sucesso !!!'}
