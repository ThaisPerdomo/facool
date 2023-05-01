import sqlite3

#### Criando a tabela (schema) #####

def cria_tabela(nome, colunas):

    with sqlite3.connect('db/user.db') as conn:
        cursor = conn.cursor()

        # Criando tabela

        cursor.execute(f""" CREATE TABLE IF NOT EXISTS {nome} (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            {colunas});""")

        # Salvando as alterações.
        conn.commit()


## Realizando consultas:

def consulta(nometabela):

    with sqlite3.connect('db/user.db') as conn:
        cursor = conn.cursor()

        cursor.execute(f'''SELECT * FROM {nometabela}''') # Selecionando todos os dados da tabela
        resultado = cursor.fetchall() # Armazenando o resultado da consulta na variável resultado
    
    ## Imprimindo o resultado em linhas:
    ## OBS: Pode-se fazer só um print(resultado), mas o resultado será impresso em uma única linha.

    for linha in resultado:
        print(linha)

### Executando qualquer comando SQL ###

def executar(comando):

    with sqlite3.connect('db/user.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f'''{comando}''')
        conn.commit()


### MANIPULANDO A TABELA USER ###

### Inserindo dados na tabela User ####

def insere_dados_usuario(nome, idade):

    with sqlite3.connect('db/user.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f'''INSERT INTO User (nome, idade) VALUES ('{nome}', {idade})''')
        conn.commit()

### Atualizando dados na tabela User ####

def atualiza_dados_usuario(set, where):

    with sqlite3.connect('db/user.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f'''UPDATE User SET {set} WHERE {where}''')
        conn.commit()

### Deletando dados na tabela User ####

def deleta_dados_usuario(where):
    
    with sqlite3.connect('db/user.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f'''DELETE FROM User WHERE {where}''')
        conn.commit()


