##Possible Questions##

I'll address your question about things people might want to calculate first. So in some sense, it feels like every
question could at least be phrased as a probability. That being said, that might not be the most natural way to
express certain ideas. Off the top of my head, there are some questions that might go more along the lines of
"How many ways can my opponent deal ten damage?" While this is very similar to a probability question and could
even almost certainly be translated into one, you asked so I delivered. That being said, I strongly suggest that you
restrain yourself to probability, and even in all likelihood some subset of probability questions. More on this to
come, but I will again stress that you shouldn't make it your job to predict all the things people will ever want to
ask. I guarantee that you can't do it. Instead, make you language as extensible as possible, which you have very
rightly emphasized.

##Language Extensibility##

So in answer to your direct question, I think it's totally unreasonable to ask a user to mess with some random
EBNF and then re-compile your Grako. On the other hand, I don't think you need to ask them to. When we talk about
extensibility, I think that we should be talking not about any old user being able to add the functionality they
want, but rather another developer expanding (or even "growing") your language to help even more users. So while I
definitely would not say that users should have to worry about how your language is implemented to that extent,
other developers that want to add functionality to your language should absolutely have to modify your code. In that
sense, you can help them most by getting a strong sense of modularity into your grammar and language structure, and
by keeping the math/probability syntax and deck definitions as separate as possible. That way, it will be clear where
(and how) to add more things to your language, and people who just want to add a different kind of deck for a new
game won't have to worry about re-doing all these probability calculations for their game. Similarly, someone who
just wants to be able to ask a question about Magic that you haven't thought of shouldn't have to worry about
stepping on the toes of the deck-creation stuff.
