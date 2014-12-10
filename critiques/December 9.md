As per request, this critique is going to be about the Math grammar. It seems like you
have a good idea about how to construct a nice, simple syntax and parse it into an AST,
so I'm not worried about you being able to make parsing work.

###Syntax Thoughts###

I have to say that I'm not super sold on the "Given <data>" part of the syntax. It's
not clear to me how that would be specified, and what it would really mean. What it
seems like you want is a way of specifying which cards from a deck are left and can
still be drawn, and it's not intuitive to me how you would do that in your current
grammar. Maybe I'm just not understanding what you want, and if that's the case then
obviously you just keep doing your thing and I'll watch it work whenever you finish.
But, it feels like there could be some smoother way of specifying which cards have been
removed from the deck, or even which cards remain. It might even be as simple as
changing the word "given", but right now it just doesn't seem clear to me how easy it
would be for me as a user to make it clear what cards were actually in play. I'm sure
some of this is just because I'm not certain what you mean by <data>.

###General Math Thoughts###

While with Deck it felt like most of the work was in getting a nice syntax/grammar
(since you were having the user define something and the only post-parser work was to
create an object holding what they defined), I think that Math will end up having a
lot of implementation issues that you will not want to deal with in the week remaining.
Spitting out an actual number will probably be harder than anticipated. Here are a few
things that jumped out to me that might not be trivial:

  * When you say "OR", it's often not clear how to combine the probabilities of the two
separate things to get the chance that one or the other happens. In the worst case,
this turns into a messy PIE problem that you may or may not remember from Discrete.

  * It might not be particularly to even get things like "AND" right when you consider
  drawing without replacement. Again, this can't simply be computed by computing two
  probabilities and multiplying, since you might use a card in both.
  
Basically, the actual math behind these computations can get really hard. I think you
can definitely get a solid grammar and maybe the counting figured out for single queries
without the complication of combining two things, but I wouldn't recommend that you
spend your time trying to get this working at a real level. It sounds like you weren't
going to try to do that anyways, but I wanted to share my opinion on where it seems like
the difficulties lie in this particular problem.
