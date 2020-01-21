# 매직매서드를 이해하고 활용해보자. 눈여겨 볼 것은, 던더 len, getitem이다.

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

print(Card)

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]




deck = FrenchDeck()

print(deck.__len__())

print(deck[0])

print(type(choice(deck).rank),choice(deck),choice(deck))

# vector 클래스를 매직매서드를 이용해 만들어보기

from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector {self.x, self.y}'

    def __abs(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(1, 1)

print(v1)