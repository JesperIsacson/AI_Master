isbtree(nil).

isbtree(t(L, _, R)):-
    isbtree(R),
    isbtree(L).