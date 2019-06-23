module Greetings where

greet :: IO ()
greet = do
    putStr "Greetings! What is your name? "
    name <- getLine
    putStr "Where are you from? "
    town <- getLine
    putStrLn "Welcome, " ++ name ++ " from " ++ town
