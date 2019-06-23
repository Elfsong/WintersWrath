-- vim: ts=4 sw=4 expandtab syntax=haskell

module Printf where

import Text.Printf

f :: Double -> String
f x = printf "<%6.3f>" x

g :: Double -> IO ()
g x = do
    printf "<%6.3f>\n" x

main :: IO ()
main = do
    let x = 123.45678
    putStrLn (f x)
    g x
