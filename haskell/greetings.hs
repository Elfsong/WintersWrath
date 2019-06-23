module Greetings where

greet :: IO ()
greet = do
    putStr "Greetings! What is your name? "
    name <- getLine
    putStr "Where are you from? "
    town <- getLine
    let msg = "Welcome, " ++ name ++ " from " ++ town
    putStrLn msg
