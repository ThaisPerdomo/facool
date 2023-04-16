class Programa: 
    def __init__(self, titulo, ano):
        self._titulo = titulo.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def titulo(self):
        return self._titulo

    @property
    def likes(self):
        return self._likes
    
    def darlike(self):
        self._likes += 1
    
    def __str__(self):
        return f'{self.titulo} - {self.ano} - {self.likes} Likes'
    ## Aqui, temos o método __str__ que é chamado quando queremos exibir o objeto Programa como uma string
   
class Filme(Programa):

    def __init__(self, titulo, ano, duracao):
        super().__init__(titulo, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f'{self.titulo} - {self.ano} - {self.duracao} min - {self.likes} Likes'
    ## Devemos sobrescrever o método __str__ da classe mãe, pois o método __str__ da classe mãe não exibe o atributo duracao

class Serie(Programa):

    def __init__(self, titulo, ano, temporadas):
        super().__init__(titulo, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.titulo} - {self.ano} - {self.temporadas} Temporadas - {self.likes} Likes'
    
filme1 = Filme('Legalmente Loira', 2003, 160)

serie1 = Serie('the office', 2001, 5)

print(f'Nome: {serie1.titulo} - Ano: {serie1.ano} - Temporadas: {serie1.temporadas}')


# # 
# # MANTER COMENTADO: Exibindo uma lista dos objetos que pertencem a classe mãe: sem o método __str__:
# #
# lista_de_programas = [filme1, serie1]

# print("Lista de programas:")

# for programa in lista_de_programas: # Aqui, criamos um loop para percorrer a lista de programas

#     # Aqui, temos um porém: o objeto filme não tem o atributo temporadas e o objeto série não tem o atributo duração
#     # Então, como podemos exibir um loop que exiba os atributos de cada objeto? Simples: usamos o hasattr()

#     atributo_classe_filha = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
#     # Aqui, atribuímos à variável atributo_classe_filha o valor do atributo duracao SE o objeto programa tiver o atributo duracao, relativo à classe Filme	
#     # Caso contrário, atribuímos o valor do atributo temporadas, relativo à classe Serie
    
#     print(f'{programa.titulo} - {atributo_classe_filha} D - {programa.likes}')

## FIM DO MANTER COMENTADO

# 
# MANTER DESCOMENTADO: Exibindo uma lista dos objetos que pertencem a classe mãe: com o uso do método __str__:
# 
lista_de_programas = [filme1, serie1]

for programa in lista_de_programas:
    print(programa)