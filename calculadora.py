#Vitória Nazareth | DRE: 121076766
#Thiago Nobre | DRE: 121086282 

import re
import numpy as np
import math as m

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

class Objetos():
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
        
    def __str__(self):
      return f'ABC =  {self.tipo}'  

#classe das operações binárias (+ - * e /)
class ExpBin():
    def __init__(self, op, exp_e, exp_d):
        self.tag = 'ExpBin'
        self.exp_d = exp_d
        self.op = op
        self.exp_e = exp_e 

#classe da operação unitária (negativo)
class ExpUni():
    def __init__(self, op, exp_e):
        self.tag = 'ExpUni'
        self.op = op
        self.exp_e = exp_e

#classe da função sqrt()
class ExpFunc():
    def __init__(self, func, exp_e):
        self.tag = "ExpFunc"
        self.func = func
        self.exp_e = exp_e

#classe das variaveis
class ExpVar():
    def __init__(self, var):
        self.tag = 'ExpVar'
        self.var = var

class ExpP():
    def __init__(self, exp):
        self.tag = 'ExpP'
        self.exp = exp

#classe do valor (atribui n)
class ExpNum():
    def __init__(self, value):
        self.tag ='ExpNum'
        self.value = value

class ExpParent():
    def __init__(self, lado_e, exp_c, lado_d):
        self.tag ='ExpParent'
        self.lado_e = lado_e
        self.exp_c = exp_c
        self.lado_d = lado_d

class ExpS():
    def __init__(self, vs, ps):
        self.tag = 'ExpS'
        self.vs = vs
        self.ps = ps

class ExpAtr():
    def __init__(self, var, valor):
        self.tag = 'ExpAtr'
        self.var = var
        self.valor = valor

#recebe uma arvore e calcula seu resultado
def Calcula_Exp(exp, dict):
    if exp.tag == 'ExpS':
        for j in range(len(exp.vs)):
            Calcula_Exp(exp.vs[j], dict)
        for j in range(len(exp.ps)):
            Calcula_Exp(exp.ps[j], dict)
    
    if exp.tag == 'ExpAtr':
        dict[exp.var] = Calcula_Exp(exp.valor, dict)

    if exp.tag == 'ExpP':
        print(Calcula_Exp(exp.exp, dict))

    #se for  apenas um número
    if exp.tag == 'ExpNum':
        return exp.value
    
    #se for uma operação de negação
    if exp.tag == 'ExpUni':
        valor = exp.exp_e
        operando = Calcula_Exp(valor,dict)
        return -operando

    #se for uma variavel
    if exp.tag == 'ExpVar':
        return dict[exp.var]

    #se for a função sqrt
    if exp.tag == 'ExpFunc':
        valor = exp.exp_e
        operando = Calcula_Exp(valor, dict)
        if exp.func == 'sqrt':
            return m.sqrt(operando)
        assert False, "Operador inválido: " + exp.op

    #se for (E)
    if exp.tag == 'ExpParent':
        valor = exp.exp_c
        operando = Calcula_Exp(valor, dict)
        return operando   

    #se uma operação binária
    if exp.tag == 'ExpBin':
        operador = exp.op
        esquerda = Calcula_Exp(exp.exp_e, dict)
        direita = Calcula_Exp(exp.exp_d, dict)

        if operador == '+':
            return esquerda + direita   
        elif operador == '-':
            return esquerda - direita
        elif operador == '/':
            return esquerda / direita
        elif operador == '*':
            return esquerda * direita
        
        

#recebe uma árvore e adiciona parenteses para tirar ambiguidade
def Parenteses_Exp(exp):

    if exp.tag == 'ExpNum':
        return str(exp.value)
    
    if exp.tag == 'ExpUni':
        valor = exp.exp_e
        operando = Parenteses_Exp(valor)
        if exp.op == '-':
            return f"{exp.op} ({operando})"
        assert False, "Operador inválido: " + exp.op

    if exp.tag == 'ExpFunc':
        valor = exp.exp_e
        operando = Parenteses_Exp(valor)
        if exp.op == 'sqrt':
            return f"({m.sqrt(operando)})"
        assert False, "Operador inválido: " + exp.op

    if exp.tag == 'ExpBin':
        operador = exp.op
        direita = Parenteses_Exp(exp.exp_d)
        esquerda = Parenteses_Exp(exp.exp_e)

        if operador == '+' or operador == '-' or operador == '/' or operador == '*':
            return f"({esquerda} {operador} {direita})"
  
        assert False, "Operador inválido: " + exp.op
        
    assert False, "Operador inválido: " + exp.op

class Parser():
    def __init__(self, tokens, next_token, i):
        self.tokens = tokens #lista
        self.next_token = next_token #(tipo, valor)
        self.i = i #posição na lista
        self.len = len(tokens)-1

    def peek(self, id):
        if self.next_token.tipo == id:
            return True
    
    def consome(self, id):
        if self.peek(id):
            token = self.next_token
            self.i += 1
            if self.i < len(self.tokens): 
                self.next_token = self.tokens[self.i]
            return token.valor
        return SyntaxError
    
    def ParseS(self):
    #S -> VS PS
        parte_V = self.ParseV()
        parte_P = self.ParseP()
        return ExpS(parte_V, parte_P)

    def ParseV(self):
    #VS ->     
    #VS -> VS <var> '=' E <newline>
        listaCalc = []
        while True:
            if self.peek("VAR"):
                var = self.consome("VAR")
                self.consome("IGUAL")
                exp = self.ParseE()
                self.consome("NEW LINE")
                listaCalc.append(ExpAtr(var, exp))
            else:
                break
        return listaCalc

    def ParseP(self):
    #PS ->
    #PS -> PS '@' E <newline>
        listaPrint = []
        while True:
            if self.peek("PRINT"):
                self.consome("PRINT")
                exp = self.ParseE()
                self.consome("NEW LINE")
                listaPrint.append(ExpP(exp))
            else:
                break
        return listaPrint
    
    def ParseE(self):
    #E -> E '+' T
    #E -> E '-' T
    #E -> T
        exp_T = self.ParseT() 
        while True: 
            if self.peek("OPERACAO"):
                if self.next_token.valor == "+" or self.next_token.valor == "-":
                    op = self.consome("OPERACAO")
                    exp_E = self.ParseE()
                    exp_T = ExpBin(op, exp_T, exp_E )
            else:
                break
        return exp_T
    
    def ParseT(self):
    #T -> T '*' F
    #T -> T '/' F
    #T -> F
        exp_F = self.ParseF()
        while True: 
            if self.peek("OPERACAO"):
                if self.next_token.valor == "*" or self.next_token.valor == "/":
                    op = self.consome("OPERACAO")
                    exp_T = self.ParseT()
                    exp_F = ExpBin(op, exp_F, exp_T)
                else: 
                    break
            else:
                break
        return exp_F
    
    #F -> '-' F
    #F -> <num>
    #F -> <var>
    #F -> <sqrt> '(' E ')'
    #F -> '(' E ')'
    def ParseF(self):
        if self.peek("OPERACAO"):
            op = self.consome("OPERACAO")
            exp = self.ParseF()
            return ExpUni(op, exp)  
        elif self.peek("NUMERO"):
            num = self.consome("NUMERO")
            return ExpNum(num)
        elif self.peek("VAR"):
            var = self.consome("VAR")
            return ExpVar(var)                
        elif self.peek("RAIZ"):
            raiz = self.consome("RAIZ")
            self.consome("SIMBOLO")
            exp = self.ParseE()
            self.consome("SIMBOLO")
            return ExpFunc(raiz, exp)
        elif self.peek("SIMBOLO"):
            simb1 = self.consome("SIMBOLO")
            exp = self.ParseE()
            simb2 = self.consome("SIMBOLO")
            return ExpParent(simb1, exp, simb2)
        elif self.peek("$"):
            return
        return SyntaxError

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

lines = readFile() 

#listinha de tuplas (TIPO, valor)
tokens = []

for j in range(len(lines)): 
    sample = lines[j]
    i = 0
    while(i < len(sample)):

        exemplo = func.match(sample, i) 
        if exemplo:
            # print('RAIZ ',exemplo.group(0))
            tokens.append(Objetos('RAIZ', exemplo.group(0)))
            i = exemplo.end()

        exemplo = iguais.match(sample, i) 
        if exemplo:
            # print('IGUAL ',exemplo.group(0))
            tokens.append(Objetos('IGUAL', exemplo.group(0)))
            i = exemplo.end()

        exemplo = operacao.match(sample, i) 
        if exemplo:
            #print('OPERACAO ',exemplo.group(0))
            tokens.append(Objetos('OPERACAO', exemplo.group(0)))
            i = exemplo.end()

        exemplo = prints.match(sample, i) 
        if exemplo:
            #print('PRINT ',exemplo.group(0))
            tokens.append(Objetos('PRINT', exemplo.group(0)))
            i = exemplo.end()

        exemplo = parenteses.match(sample, i) 
        if exemplo:
            #print('SIMBOLO ',exemplo.group(0))
            tokens.append(Objetos('SIMBOLO', exemplo.group(0)))
            i = exemplo.end()

        exemplo = identificador.match(sample, i) 
        if exemplo:
            # print('VAR ',exemplo.group(0))
            tokens.append(Objetos('VAR', exemplo.group(0)))
            i = exemplo.end()

        exemplo = quebra.match(sample, i)
        if exemplo:
            # print('NEW LINE ')
            tokens.append(Objetos('NEW LINE', exemplo.group(0)))
            i = exemplo.end()

        exemplo = branco.match(sample, i) 
        if exemplo:
            # print('ESPAÇO ')
            #tokens.append(Objetos('ESPAÇO', exemplo.group(0)))
            i = exemplo.end()

        exemplo = inteiros.match(sample, i)
        if exemplo:
            # print('NUMERO ', exemplo.group(0))
            tokens.append(Objetos('NUMERO', int(exemplo.group(0))))
            i = exemplo.end()

Calcula_Exp(Parser(tokens, tokens[0], 0).ParseS(), {})