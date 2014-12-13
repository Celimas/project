# Tyler Marklyn
# parse_math.py
# 
#
# The file containing the main method to parse a calculation list for Math
#
import g_math
import MathSemantics

def main(filename, trace=False, whitespace=None, nameguard=None):
    import json
    with open(filename) as f:
        text = f.read()
    parser = g_math.MathParser(parseinfo=False)
    print "Beginning parsing of math."
    deck = parser.parse(
        text,
        "math",   # start rule is now hard-coded as deck
        filename=filename,
        trace=trace,
        whitespace=whitespace,
        nameguard=nameguard,
        semantics=MathSemantics.MathSemantics())  # Use my semantics

    print "Result: " + str(deck)

    # Stuff for printing the AST and JSON, no longer need it
    '''
    print('AST:')
    print(ast)
    print
    print('JSON:')
    print(json.dumps(ast, indent=2))
    print
    '''

if __name__ == '__main__':
    import argparse
    import string
    import sys

    class ListRules(argparse.Action):
        def __call__(self, parser, namespace, values, option_string):
            print('Rules:')
            for r in g_deck.deckParser.rule_list():
                print(r)
            print()
            sys.exit(0)

    parser = argparse.ArgumentParser(description="Simple parser for deck.")
    parser.add_argument('-l', '--list', action=ListRules, nargs=0,
                        help="list all rules and exit")
    parser.add_argument('-n', '--no-nameguard', action='store_true',
                        dest='no_nameguard',
                        help="disable the 'nameguard' feature")
    parser.add_argument('-t', '--trace', action='store_true',
                        help="output trace information")
    parser.add_argument('-w', '--whitespace', type=str, default=string.whitespace,
                        help="whitespace specification")
    parser.add_argument('file', metavar="FILE", help="the input file to parse")
    args = parser.parse_args()

    main(
        args.file,
        trace=args.trace,
        whitespace=args.whitespace,
        nameguard=not args.no_nameguard
    )

