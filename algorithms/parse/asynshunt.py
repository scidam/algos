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
                  '!':  math.factorial  
                }

    op_func = {'sin': math.sin,
               'cos': math.cos,
               'tan': math.tan
               }

    op_precedence = {
                '+':   0,
                '-':   0,
                '*':   1,
                '/':   1,
                '(':   2,
                ')':   2,
                'sin': 2,
                'cos': 2,
                '!':   3
                    }   

    num_pat = re.compile(r'\d+|\d\.\d+')
    func_pat = re.compie(r'sin\(|cos\(|tan\(')
    op_pat  = re.compile(r'!\(\)/\*\+\-')            

    def __init__(self, exp):
        self.exp = exp
        self._op_stack = list()
        self._val_stack = list()

    def evaluate(self):
        done = False
        while not done:
            pass

    def tokenizer(self, s):
        any_pat = '(' + ''.join([self.func_pat, self.op_pat, self.num_pat]) + ')'
        any_pat.findall(s)

# ===========


