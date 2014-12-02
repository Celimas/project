# Preliminary evaluation

## What works well? What are you particularly pleased with?

I'm very pleased with using *grako* to generate parsers in Python. It's really
nice to be able to specify a grammar and have the parser pop out ready-made for
your task. All that remains is to specify semantics at that point, which is
generally not that bad.

## What could be improved? For example, how could the user's experience be
better? How might your implementation be simpler or more cohesive? 

Right now it's not really clear how the language for Deck was designed.  It is
a strange combination of English and *Generic Programming Language #3*. in that
it uses "Foreach" and things that look like functions, but then each line is
specified essentially as a sentence.

The traits part of the definition is fine, but the card specification syntax
probably needs to change dramatically because it uses "Foreach" and things that
look like functions, but then each line is specified essentially as a sentence.

Also, it would be nice if Math did anything at all... Right now it won't even
parse a file, which is something that needs to get done if the project is going
to accomplish any of its stated goals.


## Re-visit your evaluation plan from the beginning of the project. Which tools
have you used to evaluate the quality of your design? What have you learned
from these evaluations? Have you made any significant changes as a result of
these tools, the critiques, or user tests? 

Again, the traits part of Deck's definitions are great. However, I suspect that
it might be tedious to write out the cards in a deck because there is a large
amount of sort-of boilerplate sentence writing invovled in making each card in
the deck. Luckily, with grako, changing that is super easy to do, and I can
keep the same semantics and just tweak the rules. However, I will do that once
everything else is working.

My grammar for Math changes on a week-to-week basis. I want it to be easy to
request calculations as specified in my plan, but in critiquing and user
testing it has become very clear that there is no way I can ever specify
anywhere near a useful amount of predefined terms for probability calculations.

Instead, Math is now moving towards allowing users to define their own terms
such as
```
flush = 5 cards, same(suit)
pair = 2 cards, same(number)
3_of_a_kind = 3 cards, same(number)
full_house = and(pair, 3_of_a_kind)
high_card = 5 cards, different(number), not same(suit)
```
so that they can then say given a specific hand, and a certain number of draws,
what ar ethe chances they hit one of those hands. In this way, using a small
number of keywords, I can allow users to specify any number of interesting
calculations.

## Where did you run into trouble and why? For example, did you come up with
some syntax that you found difficult to implement, given your host language
choice? Did you want to support multiple features, but you had trouble getting
them to play well together? 

I ran into an interesting issue where I needed to iterate over a number of
lists that would be specified at run-time. In this problem, I was going to be
given some number of lists (of values of traits), and I needed to make a card
for all combinations of those values. However, I didn't know how many lists of
values there would be, so I couldn't just hard-code a `for` loop for each one.
I ended up solving the problem with Pythons itertools.product, which was pretty
cool.


## What's left to accomplish before the end of the project? 

Deck specification is coming along nicely, but right now Math is barely a
grammar.  By the end of the project, I need to get Math wired up with semantics
so that it can perform calculations on some basic decks, as a proof of concept.
I'd like to know that I can expand it in the future. I see this as a project I
might continue work on over winter break, or after graduation.
