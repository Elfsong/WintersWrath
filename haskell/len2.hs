module Len where

len :: [a] -> Int
len l = len2 l 0

len2 :: [a] -> Int -> Int
len2 [] lsf = lsf
len2 (x:xs) lsf = len2 xs (lsf + 1)
