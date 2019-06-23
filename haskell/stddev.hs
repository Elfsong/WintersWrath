-- vim: ts=4 sw=4 expandtab syntax=haskell

module Stddev where

square :: Double -> Double
square x = x * x

four_pass_stddev :: [Double] -> Double
four_pass_stddev xs =
    let
        count = fromIntegral (length xs)
        sum = foldl (+) 0 xs
        sumsq = foldl (+) 0 (map square xs)
    in
        (sqrt (count * sumsq - sum * sum)) / count

data StddevData = StddevData Double Double Double

one_pass_stddev :: [Double] -> Double
one_pass_stddev xs =
    let
        init_stddev_data = StddevData 0.0 0.0 0.0
        update_stddev_data (StddevData c s sq) x =
            StddevData (c + 1.0) (s + x) (sq + x*x)
        StddevData count sum sumsq =
            foldl update_stddev_data init_stddev_data xs
    in
        (sqrt (count * sumsq - sum * sum)) / count

