dict = {}



class Parser():
    def __init__(self, tokens, next_token, i):
        self.tokens = tokens #lista
        self.next_token = next_token #(tipo, valor)
        self.i = i #posição na lista

    def peek(self, id):
        if self.next_token.tipo == id:
            return True
    
    def consome(self, id):
        if self.peek(id):
            token = self.next_token
            self.i += 1
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
                listaCalc.append(ExpAtr(ExpVar(var), exp))
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
                op = self.consome("OPERACAO")
                exp_E = self.ParseE()
                exp_T = ExpBin(op, exp_E, exp_T)
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
                op = self.consome("OPERACAO")
                exp_T = self.ParseT()
                exp_F = ExpBin(op, exp_T, exp_F)
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
            if op == '-':
                return -self.ParseF()  
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


class Objetos():
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
        
    def __str__(self):
      return f'ABC =  {self.tipo}'  




lista = []
objeto1 = Objetos("IGUAL", '=')
objeto2 = Objetos("VAR", 'a') 
objeto3 = Objetos("NUMERO", 2)
lista.append(objeto1)
lista.append(objeto2)
lista.append(objeto3)



bicho = Parser(lista, lista[1], 0)

soma = bicho.ParseS()

print(soma) 





    