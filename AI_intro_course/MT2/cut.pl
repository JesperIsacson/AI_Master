split([], [], []).

split([X|L], L1, [X|L2]) :-
    \+ground(X),
    !,
    split(L, L1, L2).

split([X|L], L1, [X|L2]) :-
    var(X),
    !,
    split(L, L1, L2).

split([X|L], [X|L1], L2):-
    split(L, L1, L2).