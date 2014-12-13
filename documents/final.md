# Final Write-up

**Tyler Marklyn's final write-up for the Deck and Math languages**

## Introduction

### Motivation

There are a lot of competitive Magic the Gathering (referred to as "MtG" or "Magic" from
here out) and Hearthstone players that have to rely on often sloppy mental math
to calculate probabilities of given outcomes as they play games. Other games
such as Poker and Blackjack have been fully explored so that competitive players memorize
key numbers instead of constantly having to do difficult and time-consuming
mental math. I would like to make it easy for Hearthstone and Magic players, as
well as players of any other under-analyzed card game, to precompute
probabilities that they will need frequent access to.

A DSL is an appropriate solution for this problem because it is very easy to
textually specify a deck, given a few traits, and then all that remains is to
come up with an easy way of requesting specific forms of probability
calculations, which can also be implemented in a DSL. 

### Deck and Math in a Nutshell

Consider a game such as MtG or poker. In these games, you are often placed in a
situation where you must estimate on the spot the probability of a given
outcome. Unfortunately, this probability is often not easy to calculate. In
poker and blackjack, most/all of these probabilities have been calculated
before, so players get by on memorizing approximate probabilities of given
outcomes. However, in MtG and Hearthstone, these calcualtions have not been
run.

In order to run this sort of calculation, you need two things: a specification of
a deck to perform mathematical operations on, and a set of mathematical operations
to perform. This project will use one DSL for each of these problems.

DSLs for specifying decks of Magic cards already exist. However, they tend to
rely on a pre-existing database of Magic cards in .xml format. Since the goal
of my project is not to build a general MtG deck builder, these DSLs all have
more features than I, or users, need (such as card text), and they do not generalize well
across games. As a language, Deck attempts to boil down decks of cards to their
essentials, so that you can specify a deck with as little work as possible, and
focus more work on setting up your calculations in Math.

A program in Deck consists simply of a list of traits, and then a list of cards
that use those traits. In this way, if you keep in mind the math you are trying 
to perform, you can specify a complex deck in 20 lines or less.

Some DSLs exist that request probability calculations, mostly in
mathematical languages, but none work on 
data times that include decks of cards, so Math will be providing what is hopefully
a new and exciting set of primitives for computing probabilities on decks of cards.
Math then allows you to specify a set of queries that perform computations using 
these primitives in order to gain important information about how your deck is likely
to behave in certain key scenarios.


## Language Design Details

Writing programs in my language actually involves two languages!
 * Deck (A DSL for deck specifications): In this language, you make a text file that represents a deck of cards.
 * Math (A DSL for math on decks from Deck): In this language, you make a text file with queries you want executed on specific decks

### Deck

Deck works on stand-alone deck files, and generates instances of Deck objects in my custom Python Deck class. The Deck class uses the following main data structures
 * `Deck`: A list of `Card`s and `Trait`s present in the deck
 * `Card`: A dictionary from `Trait`s to their corresponding values
 * `Trait`: A string, and the type of the value corresponding to this trait
These data structures are reflected in the DSL, with a *Deck* being what comes out of a file when parsed, a *Trait* coming out of the `Traits:` portion of the deck declaration and *Card*s coming out of the `Cards:` portion of the deck declaration (see the Example Programs section for examples of this).

There is also one key control flow structure in the Deck language, which is a `Foreach combination of` command. These commands allow you to make a large number of cards with few lines of code, and consequently little programmer time in the Deck language. Again, one of the goals of Deck was to make it as easy as possible so that the majority of a domain expert's (in this case a competitive card game player's) time could be spend formulating the Math queries. An example use-case of a `Foreach` command is
in making a deck of standard playing cards, someone might declare it as "1 card foreach combination of suit and number." The actual syntax is slightly different than the English sentence, but this exact line shows up in the playing cards deck example in the Example Programs section.

Errors are possible in specifying decks as well. Traits are typed, but it is easy to accidently specify a potential argument
for a trait that is a number, that might not be legal. Furthermore, when you are making cards for the deck, it is possible
to specify that a card have a trait that doesn't exist, or for a card to have an invalid value on the trait. All of these errors
will get caught as Deck creates its Python *Deck* object, and throw InvalidDeckErrors with helpful error messages. Simple syntax errors will get caught by the grako parser, which sometimes produces slightly less helpful error messages.

### Math

Math will perform basic probability-based mathematical calculations on decks using SciPy. The Math language also involves a few
key data structures, namely
 * `Definition`: A way of storing specific combinations of cards to easily reference them in the future
 * `Query`: A request for a probability calculation.

 A program in the Math language first specifies what decks it wants to run on, and then it can create any number of definitions.
 Each definition is a combination of cards; for example, it might be useful to have a `pair` definition so that in your queries you don't need to type out `2x(number, Same)` every time you want to reference a pair.

 After reading its definitions, the Math language will then read and perform its queries from its file. These queries perform mathematical computations,
 and output their results in appropriate ways (Note: This language is not complete at this time, so everything else about it is
 my vision for the language, and where it might go over winter break). Some queries might have outputs in the form of plots, while others might output simple text, or csv files.

 A simple probability query has a specific structure, where the user specifies a set of known cards, and then specifies how many more cards will be drawn. At this point, the query can calculate probabilities of doing things such as "hitting a flush" or "making your third land drop" based on the probabilities of specific combinations of cards appearing after these draws, given the remaining cards in the deck.

 It is very easy to specify invalid card-combinations, and invalid mathematical operations. Each of these will throw a seperate error, all with helpful error messages.


## Example Programs

First, we see a program in Deck that specifies a deck of playing cards, with an extra 5 of clubs shuffled in. We can image this 5 of clubs has a different back than the rest of the cards, making it "Bad" if you draw it, hence the "good" trait. This program can also be found in `samples/bad_cards.deck`.
```
Traits:
    suit - Any: heart, club, diamond, spade
    number - Num: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
    good - Boolean


Cards:
    Foreach combination_of(suit, number) make(1, true)
    make(1, club, 5, false)
```
As we can see, despite the fact that the deck makes 53 cards, it is a 7-line program. Also, we show off the three possible types for traits (Any, Num or Boolean), and the "Foreach combination_of" structure, which does about what you expect it to do.

If we wanted to make a less traditional deck, here is a deck that roughly represents a legacy mono-R burn deck in MtG (this can also be found in `samples/legacy_burn.deck`).
```
Traits:
    type - Any: creature, land, spell, enchantment
    cost - Num: 0,1,2,3,4
    totheface - Boolean

Cards:
    make(16, land, 0, false)
    make(24, spell, 1, true)
    make(8, creature, 1, true)
    make(8, spell, 2, true)
    make(4, enchantment, 3, true)
```
Here we see where making more than one of a card can be useful, as many other games require large numbers of redundant cards.

Now, we see a sample query program in the Math language (from `samples/bad_poker.math`) that does some basic probability math on the bad deck of playing cards we already discussed
```
Decks: bad_cards

Definitions:
    pair = 2x(number, Same)
    3_of_a_kind = 3x(number, Same)
    4_of_a_kind = 4x(number, Same)
    flush = 5x(suit, Same)

    has_bad = (good, false)

Calculations:
    { Draws: 2
      Odds: has_bad - Not-present}

    { Draws: 5
      Odds: pair - Present}

    { Draws: 7 Odds: pair - Present }

    { Draws: 5 Odds: 3_of_a_kind - Present }

    { Cards: 2 Known: pair
      Draws: 5 Odds: 3_of_a_kind - Present }

    { Draws: 5 Odds: 4_of_a_kind - Present }

    { Draws: 7 Odds: 4_of_a_kind - Present }
```
This file will import bad_cards.deck, and then do a bunch of probability calculations. Note that all of the arguments (Cards, Known set, Draws and Odds to calculate) to a calculation are optional, with sensible default values, and that each calculation will run on every deck that is imported.

Also, in the definitions section, we see that you can specify the traits on sets of cards as being the Same (or Different), or you can specify actual values for the traits using lowercase letters (and numbers).

## Language implementation

