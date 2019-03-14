module Assignment1 (subst, interleave, unroll) where

subst :: Eq t => t ->t  -> [t] -> [t]
subst x y str = [if i==x then y else i | i <- str]

interleave :: [t] -> [t] -> [t]
interleave (x:xs) ys = x : interleave ys xs
interleave [] t = t

unroll :: Int -> [a] -> [a]
unroll x y = [y !! (i `mod` length y) | i <- [0..x-1]]
