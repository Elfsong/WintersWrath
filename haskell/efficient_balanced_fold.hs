-- vim: ts=4 sw=4 expandtab syntax=haskell

module EfficientBalancedFold where

-- more efficient version of balanced_fold which avoids
-- repeatedly scanning the list to find the length and
-- splitting it in two (creating new sub-lists)
balanced_fold' :: (e -> e -> e) -> e -> [e] -> e
balanced_fold' f b xs = fst (bal_fold1 f b xs (length xs))

-- Like balanced_fold but takes a list length len as an extra argument
-- and returns a pair (f, r), where f is the fold of the first len
-- elements of the input list and r is the rest of the input list.
bal_fold1 :: (e -> e -> e) -> e -> [e] -> Int -> (e, [e])
bal_fold1 _ b xs 0 = (b, xs)
bal_fold1 _ _ (x:xs) 1 = (x, xs)
bal_fold1 f b xs len = -- len > 1
    let
        len1 = len `div` 2
        len2 = len - len1
        (value1, rest1) = bal_fold1 f b xs len1
        (value2, rest2) = bal_fold1 f b rest1 len2
    in
        (f value1 value2, rest2)

sum_balanced :: (Num a) => [a] -> a
sum_balanced = balanced_fold' (+) 0
