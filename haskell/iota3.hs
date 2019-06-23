module Iota2 where

iota :: Int -> [Int]
iota n =
	if n == 0
	then
		[]
	else
		iota (n-1) ++ [n]
