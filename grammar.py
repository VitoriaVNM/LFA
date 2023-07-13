#Vitória Nazareth | DRE: 121076766
#Thiago Silveira | DRE: 121086282

import numpy as np
import math as m

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

#classe do valor (atribui n)
class ExpNum():
    def __init__(self, value):
        self.tag ='ExpNum'
        self.value = value


#recebe uma arvore e calcula seu resultado
def Calcula_Exp(exp, dict):

    #se for  apenas um número
    if exp.tag == 'ExpNum':
        return exp.value
    
    #se for uma operação de negação
    if exp.tag == 'ExpUni':
        valor = exp.exp_e
        operando = Calcula_Exp(valor,dict)
        if exp.op == '-':
            return -operando
        assert False, "Operador inválido: " + exp.op

    #se for uma variavel
    if exp.tag == 'ExpVar':
        return dict[exp.var]

    #se for a função sqrt
    if exp.tag == 'ExpFunc':
        valor = exp.exp_e
        operando = Calcula_Exp(valor, dict)
        if exp.op == 'sqrt':
            return m.sqrt(operando)
        assert False, "Operador inválido: " + exp.op

    #se uma operação binária
    if exp.tag == 'ExpBin':
        operador = exp.op
        direita = Calcula_Exp(exp.exp_d, dict)
        esquerda = Calcula_Exp(exp.exp_e, dict)

        if operador == '+':
            return direita + esquerda
        
        elif operador == '-':
            return direita - esquerda

        elif operador == '/':
            return direita / esquerda

        elif operador == '*':
            return direita * esquerda
        
        assert False, "Operador inválido: " + exp.op
        
    assert False, "Operador inválido: " + exp.op




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






#teste
soma = ExpBin('+',ExpVar('x'),ExpBin('*',ExpNum(2),ExpNum(3)))
dict = {'x': 1}
resultado = Calcula_Exp(soma, dict)
print(resultado) 

