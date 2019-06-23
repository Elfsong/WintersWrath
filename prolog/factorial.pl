% Several definitions of factorial with various problems or solutions

% infinite backtracking
fact1(0, 1).
fact1(N, F) :-
	N1 is N - 1,
	fact1(N1, F1),
	F is N * F1.

% fixes infinite backtracking, but still creates a choicepoint
fact2(0, 1).
fact2(N, F) :-
	N > 0,
	N1 is N - 1,
	fact2(N1, F1),
	F is F1 * N.


% no choicepoint
fact3(N, F) :-
	(   N =:= 0
	->  F=1
	;   N>0,
	    N1 is N - 1,
	    fact3(N1, F1),
	    F is F1 * N
	).

% no choicepoint, even when there should be
ap(X, Y, Z) :-
	(   X = []
	->  Z=Y
	;   X = [U|V],
	    ap(V, Y, W),
	    Z = [U|W]
	).
