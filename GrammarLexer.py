#Vitória Nazareth | DRE: 121076766
#Thiago Nobre | DRE: 121086282 

import re
                            
#grupo das variaveis
identificador = re.compile(r'[^\W0-9]([a-zA-Z0-9])*')

#grupo da função
func = re.compile(r'sqrt')

#grupos dos numeros
inteiros = re.compile(r'[0-9]+') 

#grupo dos whitespace
branco = re.compile(r' +?')

#grupo dos prints
prints = re.compile(r'^@+') #fica com os prints

#grupos dos parentese
parenteses = re.compile(r'\(|\)')

#grupo das operações
operacao = re.compile(r'\+|\-|\*|\/')

#grupo dos iguais
iguais = re.compile(r'=+?')                       

#grupo dos breakline
quebra = re.compile(r'\n') 

class Objetos():
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def __str__(self):
      return f'ABC =  {self.tipo}'  
  
def readFile():
    fileName = input('Insira o nome do arquivo: ')
    file = open(fileName, "r", encoding = 'utf8')
    return file.readlines()

lines = readFile() 

#listinha de tuplas (TIPO, valor)
tokens = []

for j in range(len(lines)): 
    sample = lines[j]
    i = 0
    while(i < len(sample)):

        exemplo = func.match(sample, i) 
        if exemplo:
            print('RAIZ ',exemplo.group(0))
            tokens.append(Objetos('RAIZ', exemplo.group(0)))
            i = exemplo.end()

        exemplo = iguais.match(sample, i) 
        if exemplo:
            print('IGUAL ',exemplo.group(0))
            tokens.append(Objetos('IGUAL', exemplo.group(0)))
            i = exemplo.end()

        exemplo = operacao.match(sample, i) 
        if exemplo:
            print('OPERACAO ',exemplo.group(0))
            tokens.append(Objetos('OPERACAO', exemplo.group(0)))
            i = exemplo.end()

        exemplo = prints.match(sample, i) 
        if exemplo:
            print('PRINT ',exemplo.group(0))
            tokens.append(Objetos('PRINT', exemplo.group(0)))
            i = exemplo.end()

        exemplo = parenteses.match(sample, i) 
        if exemplo:
            print('SIMBOLO ',exemplo.group(0))
            tokens.append(Objetos('SIMBOLO', exemplo.group(0)))
            i = exemplo.end()

        exemplo = identificador.match(sample, i) 
        if exemplo:
            print('VAR ',exemplo.group(0))
            tokens.append(Objetos('VAR', exemplo.group(0)))
            i = exemplo.end()

        exemplo = quebra.match(sample, i)
        if exemplo:
            print('NEW LINE ')
            tokens.append(Objetos('NEW LINE', exemplo.group(0)))
            i = exemplo.end()

        exemplo = branco.match(sample, i) 
        if exemplo:
            print('ESPAÇO ')
            #tokens.append(Objetos('ESPAÇO', exemplo.group(0)))
            i = exemplo.end()

        exemplo = inteiros.match(sample, i)
        if exemplo:
            print('NUMERO ', exemplo.group(0))
            tokens.append(Objetos('NUMERO', int(exemplo.group(0))))
            i = exemplo.end()



for token in tokens:
    print(token)