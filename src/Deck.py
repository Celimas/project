# Deck.py
# 
# Author: Tyler Marklyn
#
# The Python file containing the underlying data structures for the
# Deck language in my DSLs Project
#

class Deck:
    """ A datatype representing a deck of cards """
    def __init__(self):
        """ 0 argument constructor """
        self.cards = []    # A list of cards
        self.traits = {}   # A name-indexed dictionary of traits on the cards

    def addCard(self, card):
        """ Adds a card to the deck """
        self.cards.append(card)

    def addTrait(self, trait):
        """ Adds a trait to the deck """
        self.traits[trait.name] = trait

    def getValsForTrait(self, traitname):
        """ Returns a list of the possible values for the named trait """
        self.traits[traitname].vals

class Card:
    """ A datatype representing a card """
    def __init__(self):
        """ 0 argument constructor """
        self.values = {}    # A mapping of traits to values


class Trait:
    """ A datatype representing a trait """
    def __init__(self, name, t, vals):
        """ constructor """
        self.name = name    # Name should be a string
        self.t = t          # t is the type, should be "Bool", "Int" or "Any"
        self.vals = vals    # values is the possible values of the trait