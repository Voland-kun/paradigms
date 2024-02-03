sum_list([], 0).
sum_list([H|T], Sum) :-
    sum_list(T, SumT), Sum is SumT + H.

?- sum_list([1,2,3,4,5,6,7,8,9,10], X).