% rev1([], []). 

% rev1([A|BC], CBA) :-
%     rev1(BC, CB), 
%     append(CB, [A], CBA).

fact1(0, 1).

fact1(N, F) :-
    N1 is N - 1,
    fact1(N1, F1),
    F is F1 * N.

fact2(N, F) :-
    (N =:= 0 ->
        F = 1
    ; N > 0,
        N1 is N - 1,
        fact2(N1, F1),
        F is F1 * N
    ).

fact(N, F) :- 
    fact3(N, 1, F).
fact3(0, A, F) :-
    A = F.
fact3(N, A, F) :-
    N1 is N - 1,
    A1 is A * N,
    fact3(N1, A1, F).
    
append1([], C, C).
append1([A|B], C, [A|BC]) :-
    append1(B, C, BC).

% multiply(X, Y, XY) :- 
%     ( X = 0 ->
%         XY = 0
%     ; X1 is X - 1,
%     multiply(X1, Y, X1Y),
%     XY is X1Y + Y 
%     ).

multiply(X, Y, XY) :- 
    multiply_r(X, Y, 0, XY).
multiply_r(0, _, A, A).
multiply_r(X, Y, A, XY) :-
    X1 is X - 1,
    A1 is A + Y,
    multiply_r(X1, Y, A1, XY).

rec_r([], A, A).
rec_r([B|CD], A, DCBA) :-
    rec_r(CD, [B|A], DCBA).

map(_, [], []).
map(F, [X|XS], [Y|YS]) :-
    call(F, X, Y),
    map(F, XS, YS).

len1([], N, N). 
len1([_|L], N0, N) :-
    N1 is N0 + 1,
    len1(L, N1, N).