# Project plan

## Language evaluation

I will know that my language has accomplished its goals if I, and my friends in
the Magic/Hearthstone communities feel that my DSL is preferable to doing
mental math or using Excel spreadsheets. In general, this means that it will
be: 
1. Easy and *non-tedious* to specify a deck without writing out every card.
1. Easy to request certain types of common probability calculation.
1. Output from the probability DSL will be *immediately* usable by players 
   (without further processing).

Of these goals, accomplishing 1. and 2. will mean that I have *designed* my
DSLs well, because it will be easy (and hopefully fun) to write programs in.
Specifically, the non-tedium in a. emphasizes a design that does not encourage
"code reduplication" of one form or another. 

3. is more of a focus on *implementation*. This is not an input provided by a
user. Instead, it shows how well a program "runs" in my DSL, given that the
output of a program in the probability DSL is data in a human-useable form.

## Implementation plan

**Week 1:** Come up with a syntax for the deck-building DSL, and come up with
an output format for the list of cards that will be processed by the
calculation DSL. Also, come up wiht a syntax sketch for the calculation DSL,
and choose the host language for everything.

**Week 2:** Come up with a syntax for the probability calculation DSL, and an
abstract internal representation for everything. Also, decide how output will
be formatted for the probability-calculation DSL, and research methods of
generating said output.

**Week 3:** Fully implement the deck-building DSL, and begin implementation on
parsing the probability calculation DSL.

**Week 4:** Finish implementation of parsing the probability calculation DSL.
Implement evaulation of the probability calculation DSL (hopefully evaluation
is near-trivial if I've chosen my host language well.

**Week 5:** Add finishing touches to everything, work on stretch goals such as
plotted output if time permits. Add probability calculation syntax specific to
games other than Magic.

