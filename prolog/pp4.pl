:- ensure_loaded(library(clpfd)).

puzzle_solution(Puzzle) :-
    Puzzle = [_|T1],
    check_diagonal(T1),
    maplist(check_heading, T1),
    transpose(Puzzle, [_|T2]),
    maplist(check_heading, T2).

get_diagonal([], _, []).
get_diagonal([X|Xs], I, Y) :-
    nth0(I, X, E),
    append([E], R, Y),
    IN is I + 1,
    get_diagonal(Xs, IN, R).

check_heading([H|T]) :-
    all_in_range(T),
    all_different(T),
    (
        check_sum(T, H)
    ;   
        check_product(T, H)
    ).

product(X, Y, R) :- 
    R is X * Y.

check_sum(X, R) :-
    sum_list(X, R).

check_product(X, R) :- 
    foldl(product, X, 1, R).

check_diagonal(X) :-
    get_diagonal(X, 1, R), 
    all_same(R).

all_same([]).   
all_same([_]).
all_same([H, H|T]) :- 
    all_same([H|T]).

all_in_range([]).
all_in_range([H|T]) :-
   between(1, 9, H),
   all_in_range(T).