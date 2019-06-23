-- vim: ts=4 sw=4 expandtab syntax=haskell

module Unsafe where

import GHC.IOBase

f :: Int -> Int -> Int
f x y = unsafePerformIO $ do
    putStrLn ("f's arguments are " ++ (show x) ++ " " ++ (show y))
    return (x + y)
