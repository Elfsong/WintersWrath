:- ensure_loaded(borders).
:- ensure_loaded(cities).
:- ensure_loaded(countries).
:- ensure_loaded(rivers). 

larger(C1, C2) :-
        area(C1, Area1),
        area(C2, Area2),
        Area1 > Area2.

area(Country, Area) :-
        country(Country,_,_,_,Area,_,_,_).

river_country(River, Country) :-
        river(River, Countries),
        member(Country, Countries),
        country(Country).

country_region(Country, Region) :-
        country(Country,Region,_,_,_,_,_,_).
