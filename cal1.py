

INTEGER , PLUS , EOF = 'INTEGER', 'PLUS','EOF'

class Token(object):
    def __init__(self,type,value):
        #token on type integer, plus or eof
        self.type = type
        # value can be 0 to 9 , + or None
        self.value = value

    def __str__(self):
        #string representation of a class

        return 'TOKEN({type},{value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self,text):
        #client string input e.g 3+5
        self.text = text

        #index into self.text
        self.pos = 0

        #current token instance

        self.current_token = None


    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        """
        lexical analyser (scanner/tokenizer)
        responsible for breaking text into tokens

        """
        text = self.text

        if self.pos > len(text)-1 :
            return Token(EOF,None)

        current_char = text[self.pos]

        if current_char.isdigit():
            token = Token(INTEGER,int(current_char))

        elif current_char=='+':
            token = Token(PLUS,current_char)
        else:
            self.error()

        self.pos += 1
        return token


    def eat(self,token_type):

        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()

        left = self.current_token

        self.eat(INTEGER)

        op = self.current_token
        self.eat(PLUS)

        right = self.current_token
        self.eat(INTEGER)

        result = left.value + right.value

        return result


def main():

    while(True):
        try:
            text = input('calc1> ')
        except EOFError:
            break

        if not text:
            continue

        interpreter = Interpreter(text)
        result = interpreter.expr()

        print(result)

if __name__ == '__main__':
    main()
