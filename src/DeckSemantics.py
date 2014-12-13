# Tyler Marklyn
# DeckSemantics.py
#
#
# This file includes the semantics for parsing a deck object
#
#

from Deck import * 
from itertools import product
from copy import deepcopy

class InvalidDeckError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


deck_of_cards = Deck()
DEBUG = False

class DeckSemantics(object):

    def deck(self, ast):
        print "Finished processing deck."
        return deck_of_cards

    def comments(self, ast):
        if DEBUG: print "Processing traits."
        return ast

    def traits(self, ast):
        if DEBUG: print "Finished processing traits. Processing cards."
        return ast

    def trait_def(self, ast):
        traitname = str(ast['name'])
        traittype = str(ast['typevals']['type'])

        if traittype == "Boolean":
            traitvals = [True, False]

        elif traittype == "Num":
            traitvals = [ int(n) for n in ast['typevals']['vals'] ]

        elif traittype == "Any":
            traitvals = [ str(s) for s in ast['typevals']['vals'] ]
            
        else:
            raise InvalidDeckError("Invalid type on trait: " + traitname)


        t = Trait(traitname, traittype, traitvals)
        if DEBUG: print " Parsed: " + str(t)
        deck_of_cards.addTrait(t)
        return ast

    def cards(self, ast):
        if DEBUG: print "Finished processing cards"
        return ast

    def card_rule(self, ast):
        if ast['foreach'] == None:
            foreach_traits = []
        else:
            foreach_traits = [ str(s) for s in ast['foreach'] ]

        make_n = int(ast['make']['num'])
        make_values = [ getMakeVal(str(s)) for s in ast['make']['names'] ]

        # This will be the dictionary of rules generated by the make portion of the rule
        make_dict = {}
        argcounter = 0

        for trait_name in deck_of_cards.trait_names:
            if trait_name not in foreach_traits:
                value = make_values[argcounter]
                
                if not deck_of_cards.checkValidVal(trait_name, value):
                    raise InvalidDeckError(str(value) + " is not a valid value for " + trait_name)

                make_dict[trait_name] = value
                argcounter += 1

        # Now we process the foreach part of the rule
        foreach_trait_vals = [] # a list of lists of vals for the traits
        for trait_name in foreach_traits:
            foreach_trait_vals.append(deck_of_cards.getValsForTrait(trait_name))

        all_foreach_combinations = list(product(*foreach_trait_vals))

        for combo in all_foreach_combinations:
            card_dict = deepcopy(make_dict)

            # Get the values out of the combo
            for i in range(len(foreach_traits)):
                card_dict[foreach_traits[i]] = combo[i]

            if DEBUG: print "Adding " + str(make_n) + " card(s) with value(s): " + str(card_dict)

            # Make the cards
            for n in range(make_n):
                deck_of_cards.addCard(Card(card_dict))


        return ast


def getMakeVal(s):
    """ Turns a string into a make_val,
        prioritizes making bools, then ints, then strings
        Note -- It might be a little sketchy
    """
    if s == "true" or s == "True":
        return True
    if s == "false" or s == "False":
        return False
    
    try:
        return int(s)

    except ValueError:
        return s