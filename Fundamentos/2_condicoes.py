'''
As condições em python são dadas por if, elif e else
Detalhes:
  . Podemos ter if seguido de vários elif e um else final. Outro ponto é que você
  deve garantir que este else final é a última condição ou possibilidade restante de
  uma análise.
'''

'''
Exemplificando, suponha que queremos saber o imc (Índice de Massa Corporal) de uma pessoa
e seu estado na tabela de imc para analisar se ela está abaixo, acima ou no peso ideal.
'''
peso = int(input("Qual seu peso? "));
altura = float(input("Qual sua altura? "));

'''
Temos os dados de peso e altura da pessoa. Em seguida, calculamos o imc usando a fórmula:
imc é igual ao peso dividido pela altura ao quadrado.
'''
imc = peso / (altura**2);
print("Seu imc é de ", imc);
if(imc < 18.5):
  print("Você está abaixo do peso");
elif((imc >= 18.5) & (imc < 25)):
  print("Você está no peso ideal");
elif((imc >= 25) & (imc < 30)):
  print("Você está em sobrepeso");
elif((imc >= 30) & (imc < 35)):
  print("Você está em obesidade I");
elif((imc >= 35) & (imc < 40)):
  print("Você está em obesidade II");
else:
  print("Você está em obesidade III (ou Morbida)"); # Observe que esta é a última condição restante
