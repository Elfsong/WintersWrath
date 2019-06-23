-- vim: ts=4 sw=4 expandtab syntax=haskell

module Card where

data Suit = Club | Diamond | Heart | Spade
    deriving (Eq, Show)

data Rank =
    R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
    Jack | Queen | King | Ace
    deriving (Eq, Show)

data Card = Card Suit Rank
    deriving (Eq, Show)

f :: Card
f = Card Spade Ace
