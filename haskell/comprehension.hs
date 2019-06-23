-- vim: ts=4 sw=4 et ft=haskell

module Comprehension where

columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rows =    ['1', '2', '3', '4', '5', '6', '7', '8']
chess_squares = [[c, r] | c <- columns, r <- rows]

pairs = [(a, b) | a <- [1, 2, 3], b <- [1, 2, 3]]
nums  = [10*a+b | a <- [1, 2, 3], b <- [1, 2, 3], a < b]
