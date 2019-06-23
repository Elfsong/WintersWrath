-- vim: ts=4 sw=4 expandtab syntax=haskell

module Cord where

data Cord a
    = Nil
    | Leaf a
    | Branch (Cord a) (Cord a)

append_cords :: Cord a -> Cord a -> Cord a
append_cords a b = Branch a b

cord_to_list :: Cord a -> [a]
cord_to_list c = cord_to_list' c []

cord_to_list' :: Cord a -> [a] -> [a]
cord_to_list' Nil rest = rest
cord_to_list' (Leaf x) rest = x:rest
cord_to_list' (Branch a b) rest =
    cord_to_list' a (cord_to_list' b rest)

x = Branch (Branch (Leaf 1) (Leaf 2)) (Branch (Leaf 3) (Leaf 4))
