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
is_even x = if (mod x 2) == 0 then True else False

is_pos :: Int -> Bool
is_pos x = if x > 0 then True else False

is_long :: String -> Bool
is_long x = if length x > 5 then True else False
