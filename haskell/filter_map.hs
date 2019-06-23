-- vim: ts=4 sw=4 expandtab syntax=haskell

module FilterMap where

filter_map :: (a -> Bool) -> (a -> b) -> [a] -> [b]
filter_map _ _ [] = []
filter_map f m (x:xs) =
    let newxs = filter_map f m xs in
    if f x then (m x):newxs else newxs

is_even :: Int -> Bool
is_even x = (mod x 2) == 0

triple :: Int -> Int
triple x = 3 * x

one_pass :: [Int] -> [Int]
one_pass xs = filter_map is_even triple xs

two_pass :: [Int] -> [Int]
two_pass xs = map triple (filter is_even xs)
