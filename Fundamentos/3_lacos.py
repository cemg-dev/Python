'''
Um dos laços mais utilizados em python é o for enhanced.
É uma forma de escrita do for(inicialização;condição;iteração) mais intuitiva.
Isto, pois fazemos a mesma coisa do for tradicional apenas com uma variável que itera ou percorre uma lista.
'''

'''
Exemplificando, temos i como variável que itera na lista de 0 a 10 gerada pela função range.
'''
for i in range(10):
  print(i)
  
'''
Outra forma de fazermos a mesma coisa que no for é usando laços while
Detalhes:
  . O laço só inicia se a condição dentro dele for satisfeita. Assim, ele
  realiza suas iterações enquanto esta condição for satisfeita.
'''
i = 0
while(i < 10):
  print(i)
  i += 1
