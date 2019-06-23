% Prolog equivalent of Haskell flip function

% flip(Goal, X, Y) is equivalent to Goal(Y, Y).
flip(Goal, X, Y) :- call(Goal, Y, X).
