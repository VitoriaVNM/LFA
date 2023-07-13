
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
    
    def ParseV(self):
        dict = {}
        #VS -> VS <var> '=' E <newline>
        while self.peek("VAR"):
            var = self.consome("VAR")
            self.consome("IGUAL")
            exp = self.ParseE()
            dict[var] = exp   
        return dict




    