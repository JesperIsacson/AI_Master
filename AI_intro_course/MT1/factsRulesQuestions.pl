department(it, ann).
department(it, bob).
department(it, tom).
department(it, edd).
department(econ, ted).
department(econ, vic).
department(econ, joy).

role(manager, edd).
role(manager, joy).

project(p1, ann).
project(p1, bob).
project(p2, ann).
project(p2, tom).
project(p3, edd).
project(p3, ted).
project(p2, joy).
project(p4, vic).
project(p4, joy).
project(p1, edd).

projectOwner(X, Y) :-
    department(X, Z),
    role(manager, Z),
    project(Y, Z).

/*
    QUESTION 1: List all employees from a department. 
    Alternative 1:  ?- department(it, X). 
        X = ann ;
        X = bob ;
        X = tom ;
        X = edd.

    Alternative 2: -? department(econ, X).
        X = ted ;
        X = vic ;
        X = joy.


    QUESTION 2: Find all the projects each employee works on. 
    Example:  -? project(X, ann).
        X = p1 ;
        X = p2.

    Another example:  -?(X, joy).
        X = p2 ;
        X = p4.

    QUESTION 3: list the projects owned by each department. 
    Alternative 1:  -? projectOwner(it, Y).
        Y = p3 ;
        Y = p1.

    Alternative 2:  -? projectOwner(econ, Y). 
        Y = p2 ;
        Y = p4.                                                                                                                                    
*/