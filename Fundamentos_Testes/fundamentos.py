"""
MÓDULO 1: VARIÁVEIS E TIPOS DE DADOS BÁSICOS
"""

print("=== MÓDULO 1: VARIÁVEIS E TIPOS ===")

# Tipos primitivos
nome = "João Silva"          # string (str)
idade = 25                   # inteiro (int)
altura = 1.75               # ponto flutuante (float)
estudante = True            # booleano (bool)
saldo = 1500.50             # float

print(f"Nome: {nome}, Tipo: {type(nome)}")
print(f"Idade: {idade}, Tipo: {type(idade)}")
print(f"Altura: {altura}, Tipo: {type(altura)}")
print(f"É estudante: {estudante}, Tipo: {type(estudante)}")

# Conversão entre tipos
idade_texto = str(idade)
altura_inteira = int(altura)
print(f"Idade como texto: '{idade_texto}'")
print(f"Altura como inteiro: {altura_inteira}")

"""
MÓDULO 2: OPERAÇÕES MATEMÁTICAS
"""
print("\n=== MÓDULO 2: OPERAÇÕES MATEMÁTICAS ===")

a = 10
b = 3

# Operações básicas
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
resto = a % b
potencia = a ** b

print(f"Soma: {a} + {b} = {soma}")
print(f"Subtração: {a} - {b} = {subtracao}")
print(f"Multiplicação: {a} * {b} = {multiplicacao}")
print(f"Divisão: {a} / {b} = {divisao:.2f}")
print(f"Divisão inteira: {a} // {b} = {divisao_inteira}")
print(f"Resto: {a} % {b} = {resto}")
print(f"Potência: {a} ** {b} = {potencia}")

# Operações com atribuição
contador = 5
contador += 3  # Equivale a: contador = contador + 3
print(f"Contador após += 3: {contador}")

"""
MÓDULO 3: ESTRUTURAS DE DADOS
"""
print("\n=== MÓDULO 3: ESTRUTURAS DE DADOS ===")

# Listas (mutáveis)
frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]

print(f"Lista de frutas: {frutas}")
print(f"Primeira fruta: {frutas[0]}")
print(f"Última fruta: {frutas[-1]}")

# Adicionando e removendo elementos
frutas.append("uva")
frutas.insert(1, "abacaxi")
removido = frutas.pop()
print(f"Lista após modificações: {frutas}")
print(f"Fruta removida: {removido}")

# Tuplas (imutáveis)
coordenadas = (10, 20)
cores_rgb = (255, 0, 0)
print(f"Coordenadas: {coordenadas}")
print(f"Vermelho RGB: {cores_rgb}")

# Dicionários (pares chave-valor)
pessoa = {
    "nome": "Maria",
    "idade": 30,
    "cidade": "São Paulo",
    "hobbies": ["leitura", "natação", "viagem"]
}

print(f"Dicionário pessoa: {pessoa}")
print(f"Nome: {pessoa['nome']}")
print(f"Primeiro hobby: {pessoa['hobbies'][0]}")

# Adicionando nova chave
pessoa["profissao"] = "Engenheira"
print(f"Profissão adicionada: {pessoa['profissao']}")

# Conjuntos (elementos únicos)
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

print(f"Conjunto A: {conjunto_a}")
print(f"Conjunto B: {conjunto_b}")
print(f"União: {conjunto_a | conjunto_b}")
print(f"Interseção: {conjunto_a & conjunto_b}")
print(f"Diferença (A - B): {conjunto_a - conjunto_b}")

"""
MÓDULO 4: ESTRUTURAS DE CONTROLE
"""
print("\n=== MÓDULO 4: ESTRUTURAS DE CONTROLE ===")

# Condicionais
nota = 85

if nota >= 90:
    conceito = "A"
    print("Excelente!")
elif nota >= 80:
    conceito = "B"
    print("Muito bom!")
elif nota >= 70:
    conceito = "C"
    print("Bom!")
else:
    conceito = "D"
    print("Precisa melhorar!")

print(f"Nota: {nota} → Conceito: {conceito}")

# Loops - for
print("\n--- Loop for em lista ---")
for fruta in frutas:
    print(f"Fruta: {fruta}")

print("\n--- Loop for com range ---")
for i in range(3):
    print(f"Número: {i}")

print("\n--- Loop for em dicionário ---")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# Loops - while
print("\n--- Loop while ---")
contador = 3
while contador > 0:
    print(f"Contagem regressiva: {contador}")
    contador -= 1

print("Fogo!")

"""
MÓDULO 5: FUNÇÕES
"""
print("\n=== MÓDULO 5: FUNÇÕES ===")

# Função simples
def saudacao(nome):
    return f"Olá, {nome}!"

# Função com parâmetros opcionais
def calculadora(a, b, operacao='soma'):
    if operacao == 'soma':
        return a + b
    elif operacao == 'subtracao':
        return a - b
    elif operacao == 'multiplicacao':
        return a * b
    elif operacao == 'divisao':
        return a / b if b != 0 else "Erro: divisão por zero"
    else:
        return "Operação inválida"

# Função com múltiplos retornos
def analisar_numeros(lista):
    return {
        'soma': sum(lista),
        'media': sum(lista) / len(lista),
        'maior': max(lista),
        'menor': min(lista)
    }

# Testando as funções
print(saudacao("Carlos"))
print(f"Calculadora: 10 + 5 = {calculadora(10, 5)}")
print(f"Calculadora: 10 * 5 = {calculadora(10, 5, 'multiplicacao')}")

resultados = analisar_numeros([10, 20, 30, 40, 50])
print(f"Análise dos números: {resultados}")

"""
MÓDULO 6: MANIPULAÇÃO DE STRINGS
"""
print("\n=== MÓDULO 6: MANIPULAÇÃO DE STRINGS ===")

texto = "Python é uma linguagem de programação incrível"

# Métodos de string
print(f"Texto original: {texto}")
print(f"Maiúsculas: {texto.upper()}")
print(f"Minúsculas: {texto.lower()}")
print(f"Primeira letra maiúscula: {texto.capitalize()}")
print(f"Quantidade de palavras: {len(texto.split())}")
print(f"Contém 'Python'? {'Python' in texto}")
print(f"Substituindo: {texto.replace('incrível', 'poderosa')}")

# Formatação de strings
nome = "Ana"
idade = 28
mensagem = f"{nome} tem {idade} anos e ama programar em Python"
print(mensagem)

"""
MÓDULO 7: TRATAMENTO DE EXCEÇÕES
"""
print("\n=== MÓDULO 7: TRATAMENTO DE EXCEÇÕES ===")

def dividir_numeros(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Erro: Não é possível dividir por zero!"
    except TypeError:
        return "Erro: Tipos de dados inválidos!"
    finally:
        print("Operação de divisão finalizada")

# Testando o tratamento de erros
print(f"10 / 2 = {dividir_numeros(10, 2)}")
print(f"10 / 0 = {dividir_numeros(10, 0)}")
print(f"10 / 'a' = {dividir_numeros(10, 'a')}")

"""
MÓDULO 8: COMPREENSÕES E EXPRESSÕES LAMBDA
"""
print("\n=== MÓDULO 8: COMPREENSÕES E LAMBDA ===")

# List comprehension
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]
quadrados = [x**2 for x in numeros]

print(f"Números: {numeros}")
print(f"Números pares: {pares}")
print(f"Quadrados: {quadrados}")

# Dict comprehension
quadrados_dict = {x: x**2 for x in range(1, 6)}
print(f"Dicionário de quadrados: {quadrados_dict}")

# Função lambda
dobro = lambda x: x * 2
soma = lambda a, b: a + b

print(f"Dobro de 5: {dobro(5)}")
print(f"Soma de 3 + 7: {soma(3, 7)}")

# Usando lambda com map e filter
numeros_dobrados = list(map(lambda x: x * 2, numeros))
numeros_impares = list(filter(lambda x: x % 2 != 0, numeros))

print(f"Números dobrados: {numeros_dobrados}")
print(f"Números ímpares: {numeros_impares}")

"""
MÓDULO 9: PROGRAMAÇÃO ORIENTADA A OBJETOS (POO)
"""
print("\n=== MÓDULO 9: PROGRAMAÇÃO ORIENTADA A OBJETOS ===")

class Pessoa:
    # Atributo de classe
    especie = "Humano"
    
    # Construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    # Método de instância
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos"
    
    # Método estático
    @staticmethod
    def eh_adulto(idade):
        return idade >= 18
    
    # Método de classe
    @classmethod
    def informar_especie(cls):
        return f"Esta é uma instância da espécie: {cls.especie}"

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
    
    def estudar(self):
        return f"{self.nome} está estudando {self.curso}"

# Criando objetos
pessoa1 = Pessoa("João", 25)
estudante1 = Estudante("Maria", 20, "Ciência da Computação")

print(pessoa1.apresentar())
print(estudante1.apresentar())
print(estudante1.estudar())
print(f"É adulto? {Pessoa.eh_adulto(25)}")
print(Pessoa.informar_especie())

"""
MÓDULO 10: TRABALHANDO COM ARQUIVOS
"""
print("\n=== MÓDULO 10: TRABALHANDO COM ARQUIVOS ===")

# Escrevendo em arquivo
with open('exemplo.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write("Este é um arquivo de exemplo.\n")
    arquivo.write("Segunda linha do arquivo.\n")
    arquivo.write("Python é incrível!\n")

print("Arquivo 'exemplo.txt' criado com sucesso!")

# Lendo arquivo
try:
    with open('exemplo.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
        
    # Lendo linha por linha
    with open('exemplo.txt', 'r', encoding='utf-8') as arquivo:
        print("\nLinhas do arquivo:")
        for i, linha in enumerate(arquivo, 1):
            print(f"Linha {i}: {linha.strip()}")
            
except FileNotFoundError:
    print("Arquivo não encontrado!")

"""
EXEMPLO PRÁTICO: SISTEMA SIMPLES
"""
print("\n=== EXEMPLO PRÁTICO: SISTEMA DE GERENCIAMENTO ===")

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
    
    def adicionar_tarefa(self, descricao, prioridade="normal"):
        tarefa = {
            "id": len(self.tarefas) + 1,
            "descricao": descricao,
            "prioridade": prioridade,
            "concluida": False
        }
        self.tarefas.append(tarefa)
        print(f"Tarefa '{descricao}' adicionada!")
    
    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return
        
        for tarefa in self.tarefas:
            status = "✓" if tarefa["concluida"] else "✗"
            print(f"{tarefa['id']}. [{status}] {tarefa['descricao']} ({tarefa['prioridade']})")
    
    def concluir_tarefa(self, id_tarefa):
        for tarefa in self.tarefas:
            if tarefa["id"] == id_tarefa:
                tarefa["concluida"] = True
                print(f"Tarefa {id_tarefa} concluída!")
                return
        print("Tarefa não encontrada!")

# Usando o sistema
sistema = GerenciadorTarefas()
sistema.adicionar_tarefa("Aprender Python", "alta")
sistema.adicionar_tarefa("Fazer exercícios")
sistema.adicionar_tarefa("Ler documentação", "media")

print("\nLista de tarefas:")
sistema.listar_tarefas()

sistema.concluir_tarefa(1)
print("\nLista após conclusão:")
sistema.listar_tarefas()

print("\n" + "="*50)
print("🎉 PARABÉNS! Você revisou os fundamentos do Python!")
print("="*50)