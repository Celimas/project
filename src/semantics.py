# A temporary file for my semantics with post-processing
import Deck # Fix this to get the Deck.py file

class deckSemantics(object):
    deck = Deck()

    def deck(self, ast):
        print "Finished processing deck: " + deck
        return ast

    def traits(self, ast):
        print "Finished processing traits"
        return ast

    def trait_name(self, ast):
        return ast

    def trait_def(self, ast):
        traitname = "" #TODO, get name
        traittype = "" #TODO get type

        if traittype == "Boolean":
            traitvals = [True, False]

        elif traittype == "Num":
            traitvals = [1] #TODO get nums (and typecheck them)

        elif traittype == "Any":
            traitvals = [""] #TODO get strings
            
        else:
            print "Parse Error: Invalid type on trait: " + traitname
            exit(-1) #TODO learn how to do this


        t = Trait(traitname, traittype, traitvals)
        print "  Adding" + t + "to traits"
        deck.addTrait(t)
        return ast

    def typed_collection(self, ast):
        return ast

    def cards(self, ast):
        print "Finished processing cards"
        return ast

    def card_rule(self, ast):
        return ast

    def foreach_rule(self, ast):
        return ast

    def traits_rule(self, ast):
        return ast

    def combine_rule(self, ast):
        return ast

    def make_rule(self, ast):
        return ast

    def alphanumeric(self, ast):
        return ast

    def numeric(self, ast):
        return ast