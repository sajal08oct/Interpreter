

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
        integer_len = 0

        if self.pos > len(text)-1 :
            return Token(EOF,None)

        if(text[self.pos+integer_len].isdigit()):
            while(self.pos+integer_len < len(text) and text[self.pos+integer_len].isdigit()):
                integer_len+=1
        else:
            integer_len=1

        current_char = text[self.pos:self.pos+integer_len]
        # if the character is a digit then convert it to
        # integer, create an INTEGER token, increment self.pos
        # index to point to the next character after the digit,
        # and return the INTEGER token
        if current_char.isnumeric():
            token = Token(INTEGER,int(current_char))

        elif current_char=='+':
            token = Token(PLUS,current_char)
        else:
            self.error()

        self.pos += integer_len
        return token


    def eat(self,token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()


    def expr(self):
        """expr -> INTEGER PLUS INTEGER"""
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        left = self.current_token

        self.eat(INTEGER)

        op = self.current_token
        self.eat(PLUS)

        right = self.current_token
        self.eat(INTEGER)

        # at this point INTEGER PLUS INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of adding two integers, thus
        # effectively interpreting client input
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
