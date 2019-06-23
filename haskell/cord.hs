-- vim: ts=4 sw=4 expandtab syntax=haskell

module Cord where

data Cord a
    = Nil
    | Leaf a
    | Branch (Cord a) (Cord a)

append_cords :: Cord a -> Cord a -> Cord a
append_cords a b = Branch a b

cord_to_list :: Cord a -> [a]
cord_to_list Nil = []
cord_to_list (Leaf x) = [x]
cord_to_list (Branch a b) = (cord_to_list a) ++ (cord_to_list b)
