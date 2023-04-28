import sqlite3

conn = sqlite3.connect('db/user.db') 
# Criando uma conexão com o banco de dados SQLite3
# Se o banco de dados não existir, ele será criado.

cursor = conn.cursor() 
# O cursor é um objeto que permite interagir com o banco de dados contido em conn.
# Usamos o método execute() no cursor para executar um comando SQL, como visto mais adiante.


#### Criando a tabela (schema) #####

def cria_tabela(nome):
    cursor.execute(""" CREATE TABLE IF NOT EXISTS {nome} (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        idade INTEGER NOT NULL);""")

    # Salvando as alterações.
    conn.commit()


### Inserindo dados na tabela ####

# cursor.execute('''INSERT INTO User (nome, idade) VALUES ('Thais', 27)''')


## Realizando consultas:

def consulta(nometabela):
    cursor.execute(f'''SELECT * FROM {nometabela}''') # Selecionando todos os dados da tabela User
    resultado = cursor.fetchall() # Armazenando o resultado da consulta na variável resultado
    ## Imprimindo o resultado em linhas:
    ## OBS: Pode-se fazer só um print(resultado), mas o resultado será impresso em uma única linha.

    for linha in resultado:
        print(linha)


consulta("User")


# Fechando a conexão, se não fez a conexão com with.
conn.close()



