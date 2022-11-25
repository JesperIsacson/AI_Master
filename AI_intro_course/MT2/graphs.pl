%graph([a,b,c,d,e], [w(a,b,8), w(a,c,10), w(a,c,15), w(a,d,2), w(b,d,3), w(c,d,4), w(c,f,6)]).

hamiltonian(S, Graph, Path, Cost):-
    path(S, Graph, [S], K, Cost),
    reverse(K,Path).

path(S, Graph, Visited, Visited, Cost) :-
    testLength(Graph, Visited).
    
path(S, Graph, Visited, Path, Cost):-
    neighbor(S,N,Z,Graph),
    \+member(N,Visited),
    path(N, Graph,[N|Visited], Path, C),
    (integer(C) -> Cost is Z+C; Cost is Z+0).
     
neighbor(X, Y, Z, (Nodes, Edges)):-
    member(w(Y,X,Z), Edges); member(w(X,Y,Z), Edges).

testLength((Nodes, Edges), Visited):-
    sameLength(Nodes, Visited).

sameLength([],[]).
sameLength([_|L1],[_|L2]) :-
    sameLength(L1,L2).