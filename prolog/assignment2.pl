% Author: Mingzhe Du
% Student Number: 892896

% Question 1
% correspond(E1, L1, E2, L2)
correspond(X, [X|_], Y, [Y|_]).
correspond(E1, [_|Xs], E2, [_|Ys]) :-	
	correspond(E1, Xs, E2, Ys).

% Question 2
% interleave(Ls, L)
interleave(Ls, L) :-
    interLeave(Ls, L),
    sameLength(Ls).

interLeave([], []).
           
interLeave([[]|T], []) :-
    interLeave(T, []).

interLeave([[L|T]|Xs], [L|Ls]):-
    append(Xs, [T], Zs),
    interLeave(Zs, Ls).

sameLength([]).
sameLength([_]).
sameLength([E1,E2|Tail]) :-
    length(E1,N),
    length(E2,N),
    sameLength([E2|Tail]).

% Question 3
% partial eval(Expr0, Var, Val, Expr)
partial_eval(X, _, _, X) :-
    number(X).

% Handle Expression is Var
partial_eval(Expr0, Var, Val, Expr) :-
    atom(Expr0),
    ( Expr0 = Var ->
        Expr = Val
    ;
        Expr = Expr0
    ).

% Handle Expression * 
partial_eval(X*Y, Var, Val, Expr) :-
    partial_eval(X, Var, Val, E1),
    partial_eval(Y, Var, Val, E2),
    ( number(E1), number(E2) ->
        Expr is E1 * E2
    ;
        Expr = E1 * E2
    ).

% Handle Expression /
partial_eval(X/Y, Var, Val, Expr) :-
    partial_eval(X, Var, Val, E1),
    partial_eval(Y, Var, Val, E2),
    ( number(E1), number(E2) ->
        Expr is E1 / E2
    ;
        Expr = E1 / E2
    ).

% Handle Expression //
partial_eval(X//Y, Var, Val, Expr) :-
    partial_eval(X, Var, Val, E1),
    partial_eval(Y, Var, Val, E2),
    ( number(E1), number(E2) ->
        Expr is E1 // E2
    ;
        Expr = E1 // E2
    ).

% Handle Expression +
partial_eval(X+Y, Var, Val, Expr) :-
    partial_eval(X, Var, Val, E1),
    partial_eval(Y, Var, Val, E2),
    ( number(E1), number(E2) ->
        Expr is E1 + E2
    ;
        Expr = E1 + E2
    ).

% Handle Expression -
partial_eval(X-Y, Var, Val, Expr) :-
    partial_eval(X, Var, Val, E1),
    partial_eval(Y, Var, Val, E2),
    ( number(E1), number(E2) ->
        Expr is E1 - E2
    ;
        Expr = E1 - E2
    ).