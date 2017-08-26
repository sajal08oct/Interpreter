
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
