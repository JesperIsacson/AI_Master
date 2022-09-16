convert(Expression):-
    convert(Expression, Result),
    output_term(Result).

convert(Expression,Result):-
    convert_term(Expression,Result).

convert_term(le(Val1,Val2),Result) :-
    convert_term(Val1,ResultVal1),
    convert_term(Val2,ResultVal2),
    Result = (ResultVal1=<ResultVal2).

convert_term(eq(Val1,Val2),Result) :-
    convert_term(Val1,ResultVal1),
    convert_term(Val2,ResultVal2),
    Result = (ResultVal1==ResultVal2).

convert_term(ne(Val1,Val2),Result) :-
    convert_term(Val1,ResultVal1),
    convert_term(Val2,ResultVal2),
    Result = (ResultVal1=\=ResultVal2).

convert_term(ge(Val1,Val2),Result) :-
    convert_term(Val1,ResultVal1),
    convert_term(Val2,ResultVal2),
    Result = (ResultVal1>=ResultVal2).

convert_term(and(Val1,Val2),Result) :-
    convert_term(Val1,ResultVal1),
    convert_term(Val2,ResultVal2),
    Result = ResultVal1 + '&' + ResultVal2.

convert_term(or(Val1,Val2),Result) :-
    convert_term(Val1,ResultVal1),
    convert_term(Val2,ResultVal2),
    Result = ResultVal1 + '||' + ResultVal2.

convert_term(not(Val1),Result) :-
    convert_term(Val1,ResultVal1),
    Result = '!' + ResultVal1.    

convert_term(X,Result):-
    Result = X.

output_term(Val1=<Val2) :-
    write('('),
    output_term(Val1),
    write(' =< '),
    output_term(Val2),
    write(')').

output_term(Val1==Val2) :-
    write('('),
    output_term(Val1),
    write(' == '),
    output_term(Val2),
    write(')').

output_term(Val1=\=Val2) :-
    write('('),
    output_term(Val1),
    write(' <> '),
    output_term(Val2),
    write(')').

output_term(Val1>=Val2) :-
    write('('),
    output_term(Val1),
    write(' >= '),
    output_term(Val2),
    write(')').

output_term(Val1 + '&' + Val2) :-
    write('('),
    output_term(Val1),
    write(' & '),
    output_term(Val2),
    write(')').

output_term(Val1 + '||' + Val2) :-
    write('('),
    output_term(Val1),
    write(' || '),
    output_term(Val2),
    write(')').

output_term('!'+Val1) :-
    write('!'),
    output_term(Val1).

output_term(X):-
    write(X).
