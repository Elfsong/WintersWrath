-- vim: ts=4 sw=4 expandtab syntax=haskell

module Filter where

-- You cannot call this function "filter" without colliding
-- with the function named "filter" in the prelude.
filter2 :: (a -> Bool) -> [a] -> [a]
filter2 _ [] = []
filter2 f (x:xs) =
	if f x then x:fxs else fxs
	where
		fxs = filter2 f xs

is_even :: Int -> Bool
is_even x = (mod x 2) == 0

is_pos :: Int -> Bool
is_pos x = x > 0

is_long :: String -> Bool
is_long x = length x > 5

is_longer :: Int -> String -> Bool
is_longer limit x = length x > limit

evens = filter2 (\x -> (mod x 2) == 0) [1, 2, 3, 4, 5, 6]
poss  = filter2 (\x -> x > 0) [0, 1, -1, 2, -2]
longs = filter2 (\s -> length s > 5) ["ab", "abcd", "abcdef", "abcdefgh"]

n = (\a -> \b -> a * b) 3 4
