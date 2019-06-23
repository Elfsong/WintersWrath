:- use_module(library(clpfd)).

puzzle_solution(Puzzle) :-
    maplist(same_length(Puzzle), Puzzle),
    valid_puzzle(Puzzle),
    valid_diagonal(Puzzle),
    transpose(Puzzle, C_Puzzle),
    no_repeat(Puzzle), 
    no_repeat(C_Puzzle),
    valid_head(Puzzle), 
    valid_head(C_Puzzle),
    ground_vars(Puzzle).

valid_puzzle([[_|Row0]|Rows]) :-
    maplist(#=<(1), Row0),
    maplist(valid_row, Rows).

valid_row([Head|Tail]) :-
    Head #> 0,
    Tail ins 1..9.

no_repeat([_|[_|Tail]]) :-
    maplist(all_distinct, Tail).

valid_diagonal([_|Rows]) :-
    diagonal(Rows, Diagonal),
    diagonal_same(Diagonal, _).

diagonal([],[]).
diagonal([[_,A2|_]|Ts], [A2|Bs]) :-
    maplist(diagonal_tail, Ts, Ts1),
    diagonal(Ts1, Bs).

diagonal_tail([_|As], As).

diagonal_same([], _).
diagonal_same([B1|Bs], B1) :-
    diagonal_same(Bs, B1).

valid_head([_|Rows]) :- 
    maplist(row_head, Rows).

row_head([Head|Tail]) :- is_sum(Tail, Head). 
row_head([Head|Tail]) :- is_product(Tail, Head).

is_sum([],0).
is_sum([H|T], Sum) :-
    is_sum(T, Sum1),
    Sum #= H + Sum1.

is_product([],1).
is_product([H|T], Product) :-
    is_product(T, Product1),
    Product #= H * Product1.

ground_vars([_Headingrow|Rows]) :- maplist(label, Rows).