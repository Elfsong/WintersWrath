-- vim: ts=4 sw=4 expandtab syntax=haskell

module Hello where

hello :: IO ()
hello =
    putStr "Hello, "
    >>=
    \_ -> putStrLn "world!"
