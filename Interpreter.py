
INTEGER, PLUS, MINUS, DIV , MUL ,LPARAM, RPARAM, EOF = (
    'INTEGER', 'PLUS', 'MINUS', 'DIV', 'MUL' ,'(',')', 'EOF'
)

class Token(object):
    def __init__(self,type,value):
        self.type = type
        self.value = value

    def __str__(self):

        return 'Token({type},{value})'.format(
            type=self.type,
            value=self.value
        )

    def __repr__(self):
        return self.__str__()



class Lexer(object):

    def __init__(self,text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]


    def error(self):
        raise Exception('Invalid Character')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text)-1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_white_space(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        return int(result)

    def get_next_token(self):
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_white_space()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER,self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(PLUS,'+')
            if self.current_char =='-':
                self.advance()
                return Token(MINUS,'-')
            if self.current_char =='*':
                self.advance()
                return Token(MUL,'*')
            if self.current_char =='/':
                self.advance()
                return Token(DIV,'/')
            if self.current_char =='(':
                self.advance()
                return Token(LPARAM,'(')
            if self.current_char == ')':
                self.advance()
                return Token(RPARAM,')')

        return Token(EOF,None)


class Interpreter(object):

    def __init__(self,lexer):

        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()


    def error(self):
        raise Exception('Invalid Syntax')

    def eat(self,token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        if self.current_token.type == INTEGER:
            self.eat(INTEGER)
            return token.value
        if self.current_token.type == LPARAM:
            self.eat(LPARAM)
            result = self.expr()
            self.eat(RPARAM)
            return result

    def term(self):
        result = self.factor()

        while self.current_token.type in (MUL,DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
                result = result * self.factor()
            if token.type == DIV:
                self.eat(DIV)
                result = result /self.factor()

        return result


    def expr(self):
        result = self.term()
        while self.current_token.type in (PLUS,MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result = result+ self.term()
            if token.type == MINUS:
                self.eat(MINUS)
                result = result - self.term()
        return result



def main():

    while True:
        try:
            text = input('>')
        except EOFError:
            break

        if not text:
            continue

        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        try:
            print(interpreter.expr())
        except ZeroDivisionError:
            print('Division by Zero is not allowed')

if __name__ == '__main__':
    main()
