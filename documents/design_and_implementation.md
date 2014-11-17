# Language design and implementation overview

## Language design

Note: Anything that is recently new will be in *italics*

### How does a user write programs in your language (e.g., do they type in commands, use a visual/graphical tool, speak, etc.)?

Writing programs in my language has two parts
 * Deck (A DSL for deck specifications): In this language, you make a text file that represents a deck of cards.
 * Math (A DSL for math on decks from Deck): In this language, you make a text file with queries you want executed, *or you interact with a read/eval/print loop*


### What is the basic computation that your language performs (i.e., what is the computational model)?

The basic computations are also divided by mini-DSL
 * Deck: Generates a Deck object.
 * Math: In this, (probability-based) mathematical calculations are performed using SciPy.


### What are the basic data structures in your DSL, if any? How does a the user create and manipulate data?

The data structrues are as follows
 * `Deck`: A list of `Card`s and `Trait`s present in the deck
 * `Card`: A dictionary from `Trait`s to their corresponding values
 * `Trait`: A string, and the type of the value corresponding to this trait
 * `Query`: A function to be called


### What are the basic control structures in your DSL, if any? How does the user specify or manipulate control flow?

There are a few basic control structures in my DSLs, mostly taking the form of "foreach" loops.
 * Deck: Foreach is allowed for making cards (to make one for every value of a given trait), otherwise card listing is sequential.
 * Math: Foreach is allowed for doing a computation across a number of decks simultaneously
 * Math: Foreach is also allowed for doing a computation across a number of possible given initial scenarios


### What kind(s) of input does a program in your DSL require? What kind(s) of output does a program produce?

Overall, my DSLs will take two inputs: a deck file and a computations file, and then produce textual *or visual* output based on the queries in the computation file.


### Error handling: How can programs go wrong, and how does your language communicate those errors to the user?

*All of this is new, as I didn't have a good idea of what errors would exist earlier*

In Deck, it is easy to specify "illegal" decks. For example, a user could specify a trait and then not give options for it (or conversely they could give options for a trait that they didn't specify). In these scenarios, which won't be caught until runtime, I would like to try to print an error message such as 
``` No options provided for trait <trait-name>```
that makes it easy for the user to know what they need to add/remove in order to make a valid deck file.

It is also possible for syntax errors to appear in either language. In this case, I believe I will just print `syntax error` as doing more is outside the scope of this project.

In Math, it is possible to specify an invalid query (i.e., by identifying a "given" that is impossible). At this point, based on output format, I would like to give a specific error message such as 
``` Could not produce output when given(False) ```
or something similarly helpful, with the same goal as Deck of making it easy for the user to know what they need to fix quickly to get valid computations.


### What tool support (e.g., error-checking, development environments) does your project provide?

Currently, my program will provide no tool support, although a very simple expansion would be a GUI for creating decks (that could internally create the underlying `.deck` file), or a GUI with sliders/buttons for values/decks in Math.


### Are there any other DSLs for this domain? If so, what are they, and how does your language compare to these other languages? 

There exist deckbuilding DSLs for all sorts of different decks of cards. However, they are all GUI based and provide way more information about each card than is necessary for simple calculations. My DSL is different for two reasons:
 * It specifies general decks, rather than decks for a specific game
 * It is built with the idea of doing probability calculations in mind, instead of playing games in mind.


## Language implementation

### Your choice of an internal vs. external implementation and how and why you made that choice.

I chose to make an external DSL because I am not expanding a feature that already exists in a language, and therefore I find it more intuitive to design a syntax from scratch, rather than trying to design it to fit within a given host language.

### Your choice of a host language and how and why you made that choice.

I chose Python for two reasons:
 1. It's a familiar object-oriented language for development
 1. SciPy features a number of the mathematical calculations and graphical outputs I could see myself needing to perform/generate

### Any significant syntax design decisions you've made and the reasons for those decisions.

I decided a lot of invalid programs will have valid syntax and not fail until runtime. I made this decision because it is very hard to specify the same text applying at various points in a grammar (across rules). It made sense to allow for anything that could be simply parsed, and then fail at run-time when it is easy to see that an argument to a function is missing. The key here will be still providing helpful error messages.

Otherwise, I am allowing for `foreach` in both Deck and Math in order to make it easier to specify a deck, or a set of computations, in the way we think about them in our heads, rather than having to write everything out.

### An overview of the architecture of your system. 

My system works as follows:
 1. Parse the Deck file. This generates a `Deck` object in Python.
 1. Parse the Math file. This generates a list of `Query`s.
 1. For each `Query` in the list, check if it will produce valid output from the `Deck`. If it does, produce it.

At any of these steps, errors can occur. The first two will just be syntax errors with not much in the way of helpful feedback (aside from a line number). On the third, errors will be handled with graceful error messages.

