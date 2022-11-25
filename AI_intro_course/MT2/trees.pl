isbtree(nil).

isbtree(t(L, M, R)):-
    isbtree(R),
    isbtree(_,M,_),
    isbtree(L).

isbtree(_, M, _):-
    \+isbtree(M).