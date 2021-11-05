'''
Assim como as funções tornam o código mais compacto as compressões em listas fazem o mesmo só
que com estruturas de listas.
'''

'''
Exemplificando, suponha que queremos filtrar apenas os elementos >= 5 da lista abaixo 
'''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
aux = []
for i in lista:
  if(i >= 5):
    aux.append(i);

'''
Não é recomendável alterar a lista que estamos percorrendo durante o laço, então, foi necessário
criar outra lista para armazenar os valores filtrados sem contar que o código ficou um pouco grande,
pois 5 linhas de código em python deveriam fazer muito mais que apenas filtrar uma simples lista.
'''

'''
Agora reescrevendo o trecho de código acima usando compressão de listas
'''
lista = [i for i in lista if i >= 5]

'''
Com apenas uma linha e utilizando a mesma lista foi possível fazer a mesma coisa que no trecho de código
inicial.
'''

