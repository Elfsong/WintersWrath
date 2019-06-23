module Card where

data Suit = Club | Diamond | Heart | Spade

data Rank =
    R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
    Jack | Queen | King | Ace

data Card = Card Suit Rank
