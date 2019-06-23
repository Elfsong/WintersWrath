-- vim: ts=4 sw=4 expandtab syntax=haskell

module Fold where

foldl :: (v -> e -> v) -> v -> [e] -> v
foldl _ base [] = base
foldl f base (x:xs) =
    let newbase = f base x in
    Fold.foldl f newbase xs

foldr :: (e -> v -> v) -> v -> [e] -> v
foldr _ base [] = base
foldr f base (x:xs) =
    let fxs = Fold.foldr f base xs in
    f x fxs

balanced_fold :: (e -> e -> e) -> e -> [e] -> e
balanced_fold _ b [] = b
balanced_fold _ _ (x:[]) = x
balanced_fold f b l@(_:_:_) =
    let
        len = length l
        (half1, half2) = splitAt (div len 2) l
        value1 = balanced_fold f b half1
        value2 = balanced_fold f b half2
    in
        f value1 value2

suml :: (Num a) => [a] -> a
suml = Fold.foldl (+) 0

sumr :: (Num a) => [a] -> a
sumr = Fold.foldr (+) 0

productl :: (Num a) => [a] -> a
productl = Fold.foldl (*) 1

productr :: (Num a) => [a] -> a
productr = Fold.foldr (*) 1

concatl :: [[a]] -> [a]
concatl = Fold.foldl (++) []

concatr :: [[a]] -> [a]
concatr = Fold.foldr (++) []
