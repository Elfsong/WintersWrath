-- vim: ts=4 sw=4 expandtab syntax=haskell

module Showables where

data Suit = Club | Diamond | Heart | Spade
    deriving Show

data Showable = forall item . (Show item) => MkShowable item

print_showables :: [Showable] -> IO ()

print_showables [] = return ()
print_showables ((MkShowable item):xs) = do
    putStrLn (show item)
    print_showables xs

ss :: [Suit]
ss = [Club, Diamond]

wss :: [Showable]
wss = [MkShowable Club, MkShowable Diamond]

print_same_showables :: (Show a) => [a] -> IO ()

print_same_showables [] = return ()
print_same_showables (x:xs) = do
    putStrLn (show x)
    print_same_showables xs
