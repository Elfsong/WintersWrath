% Naive reverse, first version.  This does not work correctly when the
% second argument is ground and the first is free.
% Try the goal:  rev(X, [a,b,c]), and ask for more solutions after the first.
rev1([], []).
rev1([A|BC], CBA) :-
        rev1(BC, CB),
        append(CB, [A], CBA).


% Naive reverse, second version.  This works for rev(X, [a,b,c]), but not
% for the goal:  rev([a,b,c], Y).
rev2([], []).
rev2([A|BC], CBA) :-
        append(CB, [A], CBA),
        rev2(BC, CB).


% Naive reverse, third version.  This does work correctly in both directions.
% The key is to ensure that when rev1(BC, CB) is called, BC is bound.
% We do this by noting that the list and its reverse must have the same
% length.

rev3(ABC, CBA) :-
        samelength(ABC, CBA),
	rev1(ABC, CBA).


samelength([], []).
samelength([_|Xs], [_|Ys]) :-
	  samelength(Xs, Ys).
