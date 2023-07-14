dict = {}



class Parser():
    def __init__(self, tokens, next_token, i):
        self.tokens = tokens #lista
        self.next_token = next_token #(tipo, valor)
        self.i = i #posição na lista

    def peek(self, id):
        if self.next_token.tipo == id:
            return True
        #assert False, "Não tem esse tipo:" + id  
    
    def consome(self, id):
        if self.peek(id):
            self.i += 1
            self.next_token = self.tokens[self.i]
            return id
        return SyntaxError
    
    def ParseS(self):
    #S -> VS PS
        parte_V = self.ParseV()
        parte_P = self.ParseP()
        return parte_P



    def ParseV(self):
    #VS ->     
    #VS -> VS <var> '=' E <newline>
        while self.peek("VAR"):
            id = self.consome("VAR")
            self.consome("IGUAL")
            exp = self.ParseE()
            dict[id] = exp   
        return dict
    
    def ParseP(self):
    #PS ->
    #PS -> PS '@' E <newline>
        while self.peek("@"):
            id = self.consome("@")
            exp = self.ParseE()
            dict[id] = exp
        return dict
    
    def ParseE(self):
    #E -> E '+' T
    #E -> E '-' T
    #E -> T
        exp = self.ParseT() #parseT pq E precisa ir pra T antes de virar n
        while True: #why?
            if self.peek("+"):
                id = self.consome("+")
                exp_T = self.ParseT()
                #return ExpBin(id,exp,exp_T)
            elif self.peek("-"):
                id = self.consome("-")
                exp_T = self.ParseT()
                #return ExpBin(id,exp,exp_T)
            else:
                break
        return exp
    
    def ParseT(self):
    #T -> T '*' F
    #T -> T '/' F
    #T -> F
        exp = self.ParseF()
        while True: #why?
            if self.peek("*"):
                id = self.consome("*")
                exp_T = self.ParseT()
                #operando = ExpBin(id,exp,exp_T)
            elif self.peek("/"):
                id = self.consome("/")
                exp_T = self.ParseT()
                #operando = ExpBin(id,exp,exp_T)
            else:
                break
        return exp
    
    def ParseF(self):
        #exp = self.ParseF()
        while True: #why?
            if self.peek("VAR"):
                self.consome("VAR")
                id = self.tokens.valor
                self.consome("IGUAL")
                if self.peek("NUMERO"):
                    self.consome("NUMERO")
                    valor = self.tokens.valor
                    dict[id] = valor
                elif self.peek("RAIZ"):
                    self.consome("RAIZ")
                    self.consome("SIMBOLO")
                    exp = self.ParseE()
                    self.consome("SIMBOLO")

            elif self.peek("OPERACAO"):
                id = self.consome("OPERACAO")
                if id == '-':
                    operando = self.ParseF()
                    return -operando
                return SyntaxError


            else:
                break
        return exp




####################exemplinho #########################################
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
#dict = {'x': 1}

print(soma) 





    