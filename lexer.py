#Vitória Nazareth | DRE: 121076766
#Thiago Nobre | DRE: 121086282 

import re
#grupo dos comentarios
comentarios = re.compile(r'#.*?(?=\n|$)')                            

#grupo das strings
palavras = re.compile(r"r?\"(\\.|[^\\\"])*\"|r?\'(\\.|[^\\\'])*\'")                                  
 
#grupo dos identificadores
identificador = re.compile(r'[^\W0-9]([a-zA-Z0-9])*')

#grupos dos inteiros
inteiros = re.compile(r'[0-9]+')

#grupo dos whitespace
branco = re.compile(r' +?')

#grupo dos simbolos
simbolos = re.compile(r'[^a-zA-Z0-9#"\n \']+')                        

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

        exemplo = palavras.match(sample, i) 
        if exemplo:
            print('STRING ',exemplo.group(0))
            i = exemplo.end()

        exemplo = simbolos.match(sample, i) 
        if exemplo:
            print('SÍMBOLO ',exemplo.group(0))
            i = exemplo.end()

        exemplo = identificador.match(sample, i) 
        if exemplo:
            print('IDENTIFICADOR ',exemplo.group(0))
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
            print('NÚMERO', exemplo.group(0))
            i = exemplo.end()

        exemplo = comentarios.match(sample, i) 
        if exemplo:
            print('COMENTÁRIO ', exemplo.group(0))
            i = exemplo.end()
 
