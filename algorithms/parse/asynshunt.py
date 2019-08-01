"""
Shunting yard algorithm
========================

Fully asynchronous implementation of shunting-yard algorithm.


Usage
=====

Author
======
Dmitry E. Kislov
E-mail: kislov@easydan.com
"""

import asyncio
import aiohttp
import operator as op
import math
import re

#= ========    Base clases definition ===========

class Expression:
    """This is implementation of the Shunting yard algorithm proposed by E. Dejkstra"""

    op_mapping = {
                  '+':  op.add,
                  '-':  op.sub,
                  '*':  op.mul,
                  '/':  op.truediv,
                  '**': op.pow,
                }

    op_func = {'sin': math.sin,
               'cos': math.cos,
               'tan': math.tan
               }

    operators = op_mapping.keys() + op_func.keys()

    op_arity = {'+':  2,
                '-':  2,
                '**': 2,
                '*':  2,
                '/':  2,
                'sin': 1,
                'cos': 1,
                'tan': 1}

    op_precedence = {
                '+':   0,
                '-':   0,
                '*':   1,
                '/':   1,
                '(':   2,
                ')':   0,
                'sin': 1,
                'cos': 1,
                'tan': 1}   

    num_pat = r'(?:\d+|\d\.\d+)'
    func_pat = r'(?:sin|cos|tan)'
    op_pat = r'(?:\(|\)|/|\*\*|\*|\+|\-)'

    def __init__(self, expression):
        self.expression = expression
        self._op_stack = list()
        self._val_stack = list()
        self._parens = list()
        self._tokens = None

    def get_precedence(self, op):
        return self.op_precedence.get(op, None) or raise Exception("Unknown operator {}.".format(op))

    def evaluate(self):
        """Shunting  yard algorithm implementation"""

        #    I cannot implement algorithm now...
        if self._tokens is None:
            self._tokens = self.tokenizer()

        done = False
        for token in self._tokens:
            if re.match(self.num_pat, token):
                self._val_stack.append(token)
            elif token == '(':
                self._brackets.append(token)
            elif token == ')':
                # evaluate here!!!!
                c_op = ''
                while c_op != '(':
                    c_op = self._op_stack.pop()
            
            else: 
                self._op_stack.append(token)
        
        paren_count = 0

        while self._op_stack:
            c_op = self._op_stack.pop()
            if c_op == ')':
                paren_count += 1
                continue
            elif c_op == '(':
                paren_count -= 1
                continue
            elif c_op in self.operators:
                arity = self.op_arity.get(c_op)
                if arity == 2:
                    b = self._val_stack.pop()
                    a = self._val_stack.pop()
                    self._val_stack.append(self.op_func.get(c_op)(a, b))
                elif arity == 1:
                    self._val_stack.append(self.op_func.get(c_op)(self._val_stack.pop()))
                else:
                    raise Exception("Unknown arity or operator!")


    def tokenizer(self):
        any_pat = re.compile('(' + '|'.join([self.func_pat,
                                             self.op_pat,
                                             self.num_pat]) + ')')
        tokens = any_pat.findall(self.expression)
        return tokens


# ========================= main execution part ========================
def main():
    exp = Expression('3 + 6 * (2 + 6) - sin(cos(3) ** sin(4) + 8 * (1 + 2))')
    print(exp.tokenizer())
# ======================================================================


if __name__ == "__main__":
    main()