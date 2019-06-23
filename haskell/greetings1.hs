module Greetings where

greet :: IO ()
greet = do
  putStr "Greetings! What is your name? "
  >>=
  \_ -> getLine
  >>=
  \name -> (
      putStr "Where are you from? "
      >>=
      \_ -> getLine
      >>=
      \town ->
        let msg = "Welcome, " ++ name ++ " from " ++ town in
        putStrLn msg
  )
