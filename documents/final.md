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
Here are a few programs in the Deck and Math languages. Please refer to the README on the git repository for instructions on executing them.

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

I chose to make an external DSL because I am not expanding a feature that already exists in a language, and therefore I find it more intuitive to design a syntax from scratch, rather than trying to design it to fit within a given host language.
I then chose Python to implement the semantics of the language for two reasons:
 1. It's a familiar object-oriented language for development
 1. SciPy features a number of the mathematical calculations and graphical outputs I could see myself needing to perform/generate

I decided a lot of invalid programs will have valid syntax and not fail until semantics-time. I made this decision because it is very hard to specify the same text applying at various points in a grammar (across rules). It made sense to allow for anything that could be simply parsed, and then fail at run-time when it is easy to see that an argument to a function is missing. The key here will be still providing helpful error messages.

My system works as follows:
 1. Parse the Deck file. This generates a `Deck` object in Python.
 1. Parse the Math file. This generates a `Query`s as it goes.
 1. For each `Query`, check if it will produce valid output from the `Deck`. If it does, produce it.

Specifically, I implemented these steps using Grako, a Parser Generator library for Python. Grako allows you to specify a grammar, with semantic rules to be applied after a successful parse on each rule in the grammar. The grammars for Deck and Math can be found in `src/deck.grako` and `src/math.grako` respectively, with their semantics in `src/DeckSemantics.py` and `src/MathSemantics.py` respectively. These semantics objects get passed into the parser generate by grako.

### Deck implementation

In Deck, the structure of a program is very similar to the structure of the semantics. First the program specifies a list of traits that will be present, and similarly as it parses them, my parser generates *Trait* objects, which get stored in my Intermediate Representation (in the form of a *Deck* object).

Then comes the card section of the file. This section required some interesting techniques. Namely, my language allows for a
"for each combination of" construct that then takes any number of traits as arguments. Normally in Python, I would make a number of `for` loops corresponding to each trait that is an argument, but since the number of arguments is not known ahead of time, that method would not work.
Thus, I had to use a couple of cool Python features to get it to work, namely using a built-in generator that generates all possible combinations of elements in a list (which I pass in using the `*` operator), and then iterating over those to create the cards. This all happens inthe `card_rule` method in DeckSemantics. Also in that function, we see a little more magic that was requried to then iterate over all the traits that were *not* in the foreach in order to make sure that the values in the `make` portion of the rule correspond to them.

The other little bit of Python-y weirdness that needed to happen for Deck to work was the following quirk: Grako parses everything as strings, but when Traits were typed as Boolean or Number, I wanted their values to be booleans or numbers. This was simple enough to do as I was processing the trait, and had the type information right there, but when I was processing a make rule, I needed to try converting things.

This meant that I had to use my `getMakeVal` function which does a bizzare series of attempted string matches followed by a `try except` block to get everything to be the type it should be.

### Math implementation

Unfortunately, this largely does not yet exist. The parser is there, but any IR and semantics do not exist yet, as the problem ended up being larger than one I could tackle in 6 weeks.


## Evaluation

### The Good

I'm very pleased with using *grako* to generate parsers in Python. It's really
nice to be able to specify a grammar and have the parser pop out ready-made for
your task. All that remains is to specify semantics and an IR at that point, which is
generally not that bad. 

Using this scheme, Deck went from non-existent to fully-implemented in the span of about
a week and a half. It took one week to get the grammar working, and then another week
to specify the IR and the semantics, which I found it helpful to do hand-in-hand.
Namely, whenever I found myself needing a feature in Semantics (i.e. a list of traits
in the deck), I would add it to the IR, and whenever I felt like the IR should hold more
data than it was holding, it was easy to add it to the parser and the semantics in a sort
of feedback loop.

I'm fairly pleased with how Deck turned out as a result of this. The syntax could be cleaned
up in a few places, but I'm happy with the IR and the debug output, and the error handling.
I think I accomplished my goal of specifying large decks in as few lines as possible, given 
how small my deck files have ended up being (i.e. the two in the Example Programs section).

I think that moving forwards into the future of this project as a more independent project
not associated with any class, aside from a few cosmetic changes to the grammar, the majority
of the IR and the semantics for Deck will remain the same, which is a good feeling.

### The Bad

Unfortunately a week to learn grako, and then another week to get everything actually working
with grako. Seeing as the project itself only had 6 weeks to be completed, with one of these
weeks being over Thanksgiving, that did not leave me with enough time to actually tackle the 
Math language in any sort of depth.

I also lost about a week to catching up on Python, especially in terms of learning how to 
seperate code across files, and reading up on Python libaries such as SciPy. 
I haven't used Python on a project of this scale before, so I had
to learn how imports and folder packaging and such work. Overall, I feel like this portion of
the project was actually useful, despite resulting in an unfinished product
because I've always felt like Python was a great 
go-to language for small chunks of code where performance doesn't matter, and now I can 
actually make my Python code useful to future-selfs by making it modular. Also, I learned that SciPy can
do some really cool things that I'm sure I will use to satisfy my mathematical curiosities 
in the future.

That's a lot of positivity for a section labelled "The Bad", but Spaghetti Western naming schemes aside,
the fact is that Math currently parses files, and then does nothing to them (the semantics simply prints 
out the AST it parsed). I think I got a lot of productive work done, in that learning how to set things
up was a necessary part of the project, but that is a lot of stated goals that were not accomplished.

### The Ugly

I am not even particularly happy with the current state of the syntax for the Math language.
I do not think it is easily extensible to large numbers of decks, or even different output formats. The 
syntax will probably undergo a significant overhaul at some point in the future in order to make it comply 
with my stated goals of a flexible, powerful probability-calculation language on decks. Right now, it is neither
flexible, nor powerful, although I did make strides towards flexibility with the "Definitions scheme."

Also, although I believe it only requires another hour max of work (that will have to wait until after finals week),
Math won't even build Deck files currently, which was the entire original purpose of the pair of DSLs, where Deck would
pipe a deck into Math so that the calculations could be performed.

## And A Little Bit More (A final notebook entry)

Overall, with help from critique partners and an average of about 7 hours weekly of work, I was very impressed
with how much actually got done in a semester. My initial goals were a little lofty, given the intensely complicated
nature of probabilitic calculations (as pointed out by Nathan in his final critique). I think I greatly underestimated
the amount of ramp-up that is necessary at the beginning of a new project. Therefore, when I look back at my 5-week plan
from the start of the semester, I'm actually happy that I got through more than 3 weeks worth of it.

I never ran into any issue that blocked me for more than an hour or two, and along the way I solved a number of problems 
that, while they had been solved by others before, I found quite interesting. I fully intend to keep working on this DSL 
over winter break, and hopefully getting it to a point where I, and my friends, can use it as we travel around the country 
to our MtG events. 

Thank you for reading this long document on my experiences, and thanks for an opportunity to create a great and fun project!

