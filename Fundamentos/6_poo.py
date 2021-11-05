'''
A programação orientada a objetos é um dos paradigmas de programação.
Detalhes:
  . Os paradigmas que existem são: imperativo, funcional, lógico e orientado a objetos
Como diz o nome, é uma forma de programar baseando-se em objetos. Deste modo temos quatro pilares fundamentais de OO:
  . Abstração: na hora de representar dados do mundo real abstraimos informações representando apenas o necessário.
  . Encapsulamento: controlamos quem pode ou não ter acesso a certos dados de um objeto.
  . Herança: extendemos atributos e métodos de uma classe para classes filhas tornando o código mais compacto.
  . Polimorfismo: reescrevemos os métodos de uma classe mãe em uma classe filha conforme for necessário.
'''

'''
Exemplificando, suponha que queremos representar clientes e funcionários.
Detalhes:
  . O encapsulamento em python é mais complexo que em outras linguagens OO. Então,
  serão apresentados apenas Abstração, Herança e Polimorfismo.
'''

'''
Clientes e funcionários são pessoas. Então podemos criar a classe mãe Pessoa
de forma que as classes Cliente e Funcionario extenderão herdando atributos e métodos.
'''
class Pessoa:
  # Construtor da classe.
  # Toda função da classe possue self e parâmetros adicionais se houverem.
  def __init__(self, nome, idade, cpf):
    self.nome = nome;
    self.idade = idade;
    self.cpf = cpf;

  def informacoes(self):
    print("Nome: ", self.nome, ", Idade: ", self.idade, "Cpf: ", self.cpf);

# Herança 
class Cliente(Pessoa):
  def __init__(self, nome, idade, cpf, divida):
    Pessoa.__init__(self, nome, idade, cpf);
    self.divida = divida;

  # Polimorfismo
  def informacoes(self):
    print("Nome: ", self.nome, ", Idade: ", self.idade, "Cpf: ", self.cpf, "Dívida: ", self.divida);

# Herança 
class Funcionario(Pessoa):
  def __init__(self, nome, idade, cpf, salario):
    Pessoa.__init__(self, nome, idade, cpf);
    self.salario = salario;

  # Polimorfismo
  def informacoes(self):
    print("Nome: ", self.nome, ", Idade: ", self.idade, "Cpf: ", self.cpf, "Salário: ", self.salario);

c = Funcionario("Edu", 21, "12213123123", 453)
c.informacoes()
