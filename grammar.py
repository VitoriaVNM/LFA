#Vitória Nazareth | DRE: 121076766
#Thiago Silveira | DRE:

import numpy as np

'''
gramatica sugerida
E -> E + E
E -> E - E
E -> E * E 
E -> E / E
E -> - E
E -> sqrt(E)
E -> n

'''

'''
árvore para: 1+2*3
    E -> E + E
    E -> n + E * E
    E -> 1 + n * E
    E -> 1 + 2 * E
    E -> 1 + 2 * n
    E -> 1 + 2 * 3
ExpBin(ExpNum(1),'+',Expbin(ExpNum(2),'*',ExpNum(3))prox?)
árvore para: 2 - sqrt(1)
    E -> E - E
    E -> n - sqrt(E)
    E -> 2 - sqrt(E)
    E -> 2 - sqrt(n)
    E -> 2 - sqrt(1)
'''


#classe das operações binárias (+ - * e /)
class ExpBin():
    def __init__(self, exp_d, op, exp_e, prox):
        self.tag = 'ExpBin'
        self.exp_d = exp_d
        self.op = op
        self.exp_e = exp_e 
        self.prox = prox

#classe da operação unitária  (- e sqrt)
class ExpUni():
    def __init__(self, op, exp_d):
        self.tag = 'ExpUni'
        self.op = op
        self.exp_d = exp_d

#classe do valor (atribui n)
class ExpNum():
    def __init__(self, value):
        self.tag ='ExpNum'
        self.value = value

