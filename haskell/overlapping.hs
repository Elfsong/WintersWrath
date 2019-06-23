-- vim: ts=4 sw=4 expandtab syntax=haskell

module Overlapping where

data Suit = Club | Diamond | Heart | Spade
    deriving Show

class HTMLable p where
    print_as_html :: p -> IO ()

instance HTMLable Int where
    print_as_html = print_int_as_html

instance HTMLable Suit where
    print_as_html = print_suit_as_html

print_int_as_html :: Int -> IO ()
print_int_as_html x = do
    putStrLn (show x)

print_suit_as_html :: Suit -> IO ()
print_suit_as_html x = do
    putStrLn "<suit>"
    putStrLn (show x)
    putStrLn "</suit>"

instance (HTMLable a) => HTMLable [a] where
    print_as_html = print_list_as_html

instance (HTMLable a, HTMLable b) => HTMLable (a, b) where
    print_as_html = print_pair_as_html

instance (HTMLable a, HTMLable b) => HTMLable [(a, b)] where
    print_as_html = print_pair_list_as_html

print_list_as_html :: (HTMLable a) => [a] -> IO ()
print_list_as_html list = do
    putStrLn "<ul>\n"
    print_elems_as_html list
    putStrLn "</ul>\n"

print_elems_as_html :: (HTMLable a) => [a] -> IO ()
print_elems_as_html [] = return ()
print_elems_as_html (x:xs) = do
    putStrLn "<li>\n"
    print_as_html x
    print_elems_as_html xs

print_pair_as_html :: (HTMLable a, HTMLable b) => (a, b) -> IO ()
print_pair_as_html (x1, x2) = do
    print_as_html x1
    putStr " - "
    print_as_html x2

print_pair_list_as_html ::
    (HTMLable a, HTMLable b) => [(a, b)] -> IO ()
print_pair_list_as_html list = do
    putStrLn "<ul>\n"
    print_pair_elems_as_html list
    putStrLn "</ul>\n"

print_pair_elems_as_html :: (HTMLable a, HTMLable b) => [(a, b)] -> IO ()
print_pair_elems_as_html [] = return ()
print_pair_elems_as_html ((x1, x2):xs) = do
    putStrLn "<li>\n"
    putStr "("
    print_as_html x1
    putStr ", "
    print_as_html x2
    putStrLn ")"
    print_pair_elems_as_html xs

x :: IO ()
x = print_pair_list_as_html [(Club, Diamond), (Heart, Spade)]

y :: IO ()
y = print_pair_list_as_html [(1::Int, 2::Int), (3::Int, 4::Int)]
