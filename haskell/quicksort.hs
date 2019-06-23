-- vim: ts=4 sw=4 et ft=haskell

module Quicksort where

qs1 :: Ord a => [a] -> [a]

qs1 [] = []
qs1 (x:xs) = qs1(littles) ++ [x] ++ qs1(bigs)
    where
        littles = filter (<x) xs
        bigs    = filter (>=x) xs

qs2 :: Ord a => [a] -> [a]

qs2 [] = []
qs2 (x:xs) = qs2(littles) ++ [x] ++ qs2(bigs)
    where
        littles = [l | l <- xs, l < x]
        bigs    = [l | l <- xs, l >= x]

x :: [Int]
x = [20, 1, 5, 3, 4, 10]
