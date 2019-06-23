module Allpos where

all_pos :: [Int] -> Bool

all_pos [] = True
all_pos (x:xs) = x > 0 && all_pos xs
