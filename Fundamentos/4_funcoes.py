'''
No desenvolvimento de software é importante programar os trechos de código da forma mais compacta e legível possível.
Por isso, podemos programar trechos de código como funções podendo de certa forma acessar ou utilizar estes
trechos de código com uma simples chamada de função.
'''

'''
Exemplificando, suponha que utilizamos várias vezes o cálculo da média em um programa. Não seria interessante um código
da seguinte forma:
  lista_01 = [1, 2, 3];
  media_01 = sum(lista_01) / len(lista_01)
  
  lista_02 = [2, 3, 4];
  media_02 = sum(lista_02) / len(lista_02)
  
  lista_03 = [3, 4, 6];
  media_03 = sum(lista_03) / len(lista_03)
  
  lista_04 = [3, 4, 5];
  media_04 = sum(lista_04) / len(lista_04)
'''
def media(lista):
  return (sum(lista) / len(lista));

'''
Observe que o código fica mais compacto e legível quando utilizamos funções. Este exemplo
foi um pouco fraco, mas na maioria dos casos a diferença entre um código com inúmeros trechos
repetidos e um código compacto que utiliza funções será facilmente percepitível.
'''
lista_01 = [1, 2, 3];
media_01 = media(lista_01);

lista_02 = [2, 3, 4];
media_01 = media(lista_01);

lista_03 = [3, 4, 6];
media_01 = media(lista_01);

lista_04 = [3, 4, 5];
media_01 = media(lista_01);
