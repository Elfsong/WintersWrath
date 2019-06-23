module Len where

-- len1 :: [a] -> Int
-- len1 []     = 0
--   len1 (x:xs) = 1 + len1 xs

len2 :: [a] -> Int
len2 [] =
    0
len2 (x:xs) =
    1 +
    len2 xs

