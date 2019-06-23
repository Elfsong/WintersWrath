-- vim: ts=4 sw=4 expandtab syntax=haskell

module Sorted where

sorted1 :: (Ord a) => [a] -> Bool
sorted1 [] = True
sorted1 (_:[]) = True
sorted1 (x1:x2:xs) =
    x1 <= x2 && sorted1 (x2:xs)

sorted2 :: (Ord a) => [a] -> Bool
sorted2 [] = True
sorted2 (x:xs) = sorted_lag x xs

sorted_lag :: (Ord a) => a -> [a] -> Bool
sorted_lag _ [] = True
sorted_lag x1 (x2:xs) =
    x1 <= x2 && sorted_lag x2 xs
