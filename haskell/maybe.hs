-- vim: ts=4 sw=4 expandtab syntax=haskell

module MaybeMonad where

import Data.Maybe

maybe_head :: [a] -> Maybe a
maybe_head [] = Nothing
maybe_head (x:_) = Just x

maybe_sqrt :: Double -> Maybe Double
maybe_sqrt x =
    if x >= 0 then Just (sqrt x) else Nothing

maybe_sqrt_of_head :: [Double] -> Maybe Double
maybe_sqrt_of_head l = maybe_head l >>= maybe_sqrt

maybe_sqrt_of_head' l = 
    let mh = maybe_head l in
    case mh of
        Nothing -> Nothing
        Just h -> maybe_sqrt h
