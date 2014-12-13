# Deck and Math

## Tyler Marklyn's DSL(s)

### Setting Up and Running

**1. Compiling the parsers**
If this is your first checkout of this repo (or you have been fiddling with
the grako parsers), you will need to compile the parsers. In order to do so,
navigate to the `src` directory, and run
```
./compile_parsers.sh
```
which should (re)compile the paresrs.

**2. Using Deck**
If all you want to do is make sure you wrote your deck correctly, and see
some stats about your deck, you can run the command (from the root of the repo)
```
python DeckLanguage.py <path-to-deck-file>
```
This will parse your deck, and print out the traits and cards as it creates
them, with a breif summary of the entire deck at the end.

**3. Using Math**
If you want to get the full functionality out of Deck and Math, you
can run the following command from the root of the repo
```
python MathLanguage.py <path-to-math-file>
```
This will run your math file, which involves first parsing all of the deck
files named as decks at the top of the .math file, and then performing
your math queries on these decks.

Unfortunately, at this time Math is not fully implemented, so all this command will do is
parse the .math file without doing anything else.

