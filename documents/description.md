# Project description and plan

My project: Mathematical Summaries of Decks of Cards


## Motivation

There are a lot of Magic the Gathering (referred to as "MtG" or "Magic" from
here out) and Hearthstone players that have to rely on often sloppy mental math
to calculate probabilities of given outcomes as they play games. Other games
such as Poker and Blackjack have been fully explored so that players memorize
key numbers instead of constantly having to do difficult and time-consuming
mental math. I would like to make it easy for Hearthstone and Magic players, as
well as players of any other under-analyzed card game, to precompute
probabilities that they will need frequent access to.

A DSL is an appropriate solution for this problem because it is very easy to
textually specify a deck, given a few traits, and then all that remains is to
come up with an easy way of requesting specific forms of probability
calculations, which can also be implemented in a DSL. 

## Language domain

My project is useful for anyone who is interested in learning mathematical
probabilities of specific outcomes, given a deck of specified cards.
Applications for this include: Poker, Blackjack, Magic the Gathering and
Hearthstone, among others. In all of these games, you are often placed in a
situation where you must estimate on the spot the probability of a given
outcome. Unfortunately, this probability is often not easy to calculate. In
poker and blackjack, most/all of these probabilities have been calculated
before, so players get by on memorizing approximate probabilities of given
outcomes. However, in MtG and Hearthstone, these calcualtions have not been
run.

Technically, I this actually involves two DSLs: One for specifying decks of
cards with specific traits, and one for requesting probability calculations.
DSLs for specifying decks of Magic cards already exist. However, they tend to
rely on a pre-existing database of Magic cards in .xml format. Since the goal
of my project is not to build a general MtG deck builder, these DSLs all have
more features than I need (such as card text), and they do not generalize well
to other games. As for DSLs that request probability calculations, some
mathematical languages have probability calculations built in, but not on decks
of cards, so this is also something that will come mostly from scratch.


## Language design

A program in the deck specification DSL is essentially a list of cards and
traits, with the goal of simplicity. However, a deck on its own is not good for
much (although you can see how many cards are in it). The DSL might have a few
interesting features such as one that makes it easy to specify which
combinations of traits are present in a deck, without needing to specify each
card individually but no mathematical computation will be performed by this
DSL.  


The probability calculation DSL will have programs that take the form of
queries. When these programs run, they will perform mathematical calculations
and provide results to the user either in the form of plots, data that can be
plotted in something like Excel, or plain text. For outputting to Excel, csv
files might represent an easy way to output portable data.


## Example computations

I should be able to specify a standard deck of playing cards with something
like (syntax still subject to much change):

Deck = Playing Cards
Traits = {suit, number}
Card = 1x each combination of suit and number
suit = {heart, club, diamond, spade}
number = {1,2,3,4,5,6,7,8,9,10,11,12,13}

As can be seen, I did not have to write out all 52 standard playing cards,
which was the goal, given that most Magic decks have 40+ cards, and Heathstone
decks have 30 cards that could be tedious to write out in their entirety.


The probability calculation DSL will process requests such as: "Given decks
1-5, which is the most likely to have two lands in 10 cards?" or "What is the
probability that deck 6 will draw a taunt creature on turn 13?". The DSL will
convert the request into a mathematical equation, and then run the appropriate
calculation, and give results. Ideally, it will also be able to handle a
request such as "Plot the probabilities of decks 1-10 to have a land in 7-15
cards", which is a common quesiton asked by magic players, which currently
tends to be answered by hand-entering a large quantity of numbers into excel
spreadsheets in order to perform calculations. Hopefully, this DSL could reduce
the need for hard-to-decipher spreadhseets.

