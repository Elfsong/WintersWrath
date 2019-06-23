-- vim: ts=4 sw=4 expandtab syntax=haskell

module Append where

append :: [a] -> [a] -> [a]
append [] ys = ys
append (x:xs) ys = x:(append xs ys)

append_lists :: [[a]] -> [a]
append_lists [] = []
append_lists [l:ls] = l ++ (append_lists ls)

append_lists_bad :: [[a]] -> [a]
append_lists_bad [] = []
