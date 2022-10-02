%graph([a,b,c,d,e], [w(a,b,8), w(a,c,10), w(a,c,15), w(a,d,2), w(b,d,3), w(c,d,4), w(c,e,6)]).

hamiltonian(S, Graph, Path, Cost):-
    path(S, Graph, [S], K).
    
    
path(S, Graph, Visited, Path):-
    neighbor(S,N,Graph),
    \+member(N,Visited),
    write(N),
    path(N,Graph,Visited,Path).

neighbor(X, Y, (Nodes, Edges)):-
    member(w(X,Y,Z), Edges);member(w(Y,X,Z), Edges).