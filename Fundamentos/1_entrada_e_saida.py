'''
As funções input e print são responsáveis pela entrada e saída, respectivamente
Detalhes:
    . input sempre retorna uma string
    . print imprime os dados
'''
nome = input("Qual seu nome? ");
print("Olá, ", nome);

'''
E se quisermos converter uma string para int?
'''
idade = int(input("Qual a sua idade? "));
print("Você tem ", idade, "anos de idade");

'''
E se quisermos converter uma string para float?
'''
salario = float(input("Qual o seu salário mensal? "))
print("Você ganha ", salario, "mensalmente");
