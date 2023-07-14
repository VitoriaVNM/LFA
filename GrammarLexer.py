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

#grupos dos parenteses e operações
simbolo = re.compile(r'[^a-zA-Z0-9#"\n \']+?')

#grupo dos iguais
iguais = re.compile(r'=+?')                       

#grupo dos breakline
quebra = re.compile(r'\n') 


def readFile():
    fileName = input('Insira o nome do arquivo: ')
    file = open(fileName, "r", encoding = 'utf8')
    return file.readlines()

lines = readFile() 

for j in range(len(lines)): 
    sample = lines[j]
    i = 0
    while(i < len(sample)):

        exemplo = func.match(sample, i) 
        if exemplo:
            print('RAIZ ',exemplo.group(0))
            i = exemplo.end()

        exemplo = iguais.match(sample, i) 
        if exemplo:
            print('IGUAL ',exemplo.group(0))
            i = exemplo.end()

        exemplo = prints.match(sample, i) 
        if exemplo:
            print('PRINT ',exemplo.group(0))
            i = exemplo.end()

        exemplo = simbolo.match(sample, i) 
        if exemplo:
            print('SIMBOLO ',exemplo.group(0))
            i = exemplo.end()

        exemplo = identificador.match(sample, i) 
        if exemplo:
            print('VAR ',exemplo.group(0))
            i = exemplo.end()

        exemplo = quebra.match(sample, i)
        if exemplo:
            print('NEW LINE ')
            i = exemplo.end()

        exemplo = branco.match(sample, i) 
        if exemplo:
            print('ESPAÇO ')
            i = exemplo.end()

        exemplo = inteiros.match(sample, i)
        if exemplo:
            print('NÚMERO ', exemplo.group(0))
            i = exemplo.end()
        
