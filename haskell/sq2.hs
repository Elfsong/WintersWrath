-- vim: ts=4 sw=4 expandtab syntax=haskell

module Squares where

main ::IO ()
main = do
    putStrLn "Table of squares:"
    let row_actions = map show_entry [1..15]
    execute_actions (take 10 row_actions)

table_entry :: Int -> String
table_entry n = (show n) ++ "^2 = " ++ (show (n*n))

show_entry :: Int -> IO ()
show_entry n = do putStrLn (table_entry n)

execute_actions :: [IO ()] -> IO ()
execute_actions [] = return ()
execute_actions (x:xs) = do
    x
    execute_actions xs
