from PascalInterpreter.Lexer import *


class AST(object):
    pass

class BinOp(AST):
    def __init__(self,left,op,right):
        self.left = left
        self.token=self.op = op
        self.right=right



class Num(AST):
    def __init__(self,token):
        self.token = token
        self.value =token.value


class Parser(object):
    def __init__(self,lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()


    def error(self):
        raise Exception('Invalid Syntax')


    def eat(self,token_type):

        if(self.current_token.type == token_type):
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token

        if token.type ==INTEGER:
            self.eat(INTEGER)
            return Num(token)
        elif token.type==LPARAM:
            self.eat(LPARAM)
            node = self.expr()
            self.eat(RPARAM)

            return node

    def term(self):
        node = self.factor()

        while self.current_token.type in (MUL,DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
            else:
                self.eat(DIV)

            node = BinOp(left= node,op=token,right=self.factor())

        return node


    def expr(self):
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def parse(self):
        return self.expr()