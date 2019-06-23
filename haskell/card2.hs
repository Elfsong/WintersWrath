module Card where

data Suit = Club | Diamond | Heart | Spade

data Rank =
    R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
    Jack | Queen | King | Ace

data Card = Card Suit Rank

showrank :: Rank -> String
showrank R2    = "R2"
showrank R3    = "R3"
showrank R4    = "R4"
showrank R5    = "R5"
showrank R6    = "R6"
showrank R7    = "R7"
showrank R8    = "R8"
showrank R9    = "R9"
showrank R10   = "R10"
showrank Jack  = "Jack"
showrank Queen = "Queen"
showrank King  = "King"
showrank Ace   = "Ace"

instance Show Rank where show = showrank
