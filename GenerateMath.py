#!/usr/bin/env python3
import random
from copy import deepcopy
import sys

class Range:
    '''number range for operation. lo and hi are both included'''
    def __init__(self, lo, hi):
        self.lo = lo
        self.hi = hi

    def getNum(self):
        return random.randint(self.lo, self.hi)

class MathOp:
    '''
    Base class of operators
    '''
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.ans = None

    def out(self, op: str):
        return '%d %s %d =' %(self.a, op, self.b)


class Add(MathOp):
    def __init__(self, rangeA: Range, rangeB: Range):
        a , b = rangeA.getNum(), rangeB.getNum()
        super().__init__(a, b)
        self.ans = a + b

    def out(self):
        return super().out('+')


class Minus(MathOp):
    def __init__(self, rangeA: Range, rangeB: Range):
        a , b = rangeA.getNum(), rangeB.getNum()
        super().__init__(a, b)
        self.ans = a - b

    def out(self):
        return super().out('-')


class Multiply(MathOp):
    def __init__(self, rangeA: Range, rangeB: Range):
        a , b = rangeA.getNum(), rangeB.getNum()
        super().__init__(a, b)
        self.ans = a * b

    def out(self):
        return super().out('·')


class Devide(MathOp):
    '''
    rangeA and rangeB are range for ratio and divisor
    '''
    def __init__(self, rangeA: Range, rangeB: Range):
        a , b = rangeA.getNum(), rangeB.getNum()
        c = a * b
        super().__init__(c, b)
        self.ans = a

    def out(self):
        return super().out(':')

def getQA(mathOp, N, rangeA, rangeB):
    '''
    :return
    '''
    return [deepcopy(mathOp(rangeA, rangeB)) for i in range(N)]

if __name__ == '__main__':
    questionName, answerName = sys.argv[1:3]
    range10 = Range(2, 10)
    range100 = Range(2, 100)
    range1000 = Range(2, 1000)
    range10_1000 = Range(10, 1000)
    range10_100 = Range(10, 100)
    # qas = \
    #     getQA(Multiply, 7, range10_100, range10_100) + \
    #     getQA(Add, 6, range10_1000, range10_1000) + \
    #     getQA(Devide, 6, range100, range10) + \
    #     getQA(Minus, 6, range10_1000, range10_1000)
    qas = getQA(Multiply, 5, range10_1000, range10_1000) + getQA(Multiply, 20, range10_100, range10_100)
    random.shuffle(qas)
    with open(questionName, 'w') as q:
        q.writelines(['( %d )  %s\n' %(i+1, qa.out())for i, qa in enumerate(qas)])

    with open(answerName, 'w') as q:
        q.writelines(['( %d )  %s\n' %(i+1, qa.ans)for i, qa in enumerate(qas)])
