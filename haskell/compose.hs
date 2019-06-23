module Compose where

min :: (Ord t) => [t] -> Maybe t

min = maybehead . mergesort

maybehead :: [t] -> Maybe t
maybehead [] = Nothing
maybehead (x:_) = Just x

merge :: Ord a => [a] -> [a] -> [a]
merge [] ys = ys
merge (x:xs) [] = x:xs
merge (x:xs) (y:ys)
       | x <= y = x : merge xs (y:ys)
       | x >  y = y : merge (x:xs) ys

to_single_els :: [a] -> [[a]]
to_single_els [] = []
to_single_els (x:xs) = [x] : to_single_els xs

merge_consec :: Ord a => [[a]] -> [[a]]
merge_consec [] = []
merge_consec [xs] = [xs]
merge_consec (xs1:xs2:xss) = (merge xs1 xs2) : merge_consec xss

repeat_merge_all :: Ord a => [[a]] -> [a]
repeat_merge_all [] = []
repeat_merge_all [xs] = xs
repeat_merge_all xss@(_:_:_) =
               repeat_merge_all (merge_consec xss)

mergesort :: Ord a => [a] -> [a]
mergesort xs =
       repeat_merge_all (merge_consec (to_single_els xs))
