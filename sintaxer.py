dict = {}

class Parser():
    def __init__(self, tokens, next_token, i):
        self.tokens = tokens #lista
        self.next_token = next_token #(tipo, valor)
        self.i = i #posição na lista

    def peek(self, id):
        if self.next_token.id == id:
            return True
        assert False, "Não tem esse tipo:" + id  
    
    def consome(self, id):
        if self.peek(id):
            self.i += 1
            self.next_token = self.tokens[self.i]
            return id
        return SyntaxError
    
    def ParseS(self):
    #S -> VS PS
        self.ParseV()
        self.ParseP()


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
    #F -> '-' F
    #F -> <num>
    #F -> <var>
    #F -> <sqrt> '(' E ')'
    #F -> '(' E ')'
        #exp = self.ParseF()
        while True: #why?
            if self.peek("VAR"):
                id = self.consome("VAR")
                #variavel = ExpVar(id)
            elif self.peek("NUMERO"):
                id = self.consome("NUMERO")

            elif self.peek("RAIZ"):
                id = self.consome("RAIZ")
                
         
            elif self.peek("-"):
                id = self.consome("-"):
                operando = self.ParseF()
                return -operando
                #numero = ExpNum(id)
            else:
                break
        return exp








    