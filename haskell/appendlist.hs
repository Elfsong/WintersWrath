-- vim: ts=4 sw=4 expandtab syntax=haskell

module Appendlist where

data Cord a
    = Nil
    | Leaf a
    | Branch (Cord a) (Cord a)
    deriving Show -- for testing

-- Need -fglasgow-exts since this is multi-parameter

class Appendlist c a where
    empty ::  c a
    cons ::   a -> c a -> c a
    append ::  c a -> c a -> c a
    is_empty ::  c a -> Bool
    decons ::  c a -> (a, c a)

instance Appendlist [] a where
    empty = []
    cons = (:)
    append = (++)
--  is_empty = (==[])  -- compiler complains we need Eq a
    is_empty = is_empty_list
    decons = \(x:xs) -> (x, xs)  -- pattern matching with lambda is supported
--  decons = \xs -> (head xs, tail xs)

is_empty_list [] = True
is_empty_list (_:_) = False

instance Appendlist Cord a where
    empty = Nil
    cons = cord_cons
    append = Branch
    is_empty = cord_is_empty
    decons = cord_decons

cord_cons :: a -> Cord a -> Cord a
cord_cons x xs = Branch (Leaf x) xs

cord_is_empty :: Cord a -> Bool
cord_is_empty Nil = True
cord_is_empty (Leaf _) = False
cord_is_empty (Branch ls rs) = cord_is_empty ls && cord_is_empty rs

cord_decons :: Cord a -> (a, Cord a)
cord_decons Nil = error "decons of empty cord"
cord_decons (Leaf a) = (a, Nil)
cord_decons (Branch Nil as) = cord_decons as
cord_decons (Branch (Leaf a) as) = (a, as)
cord_decons (Branch (Branch as bs) cs) = cord_decons (Branch as (Branch bs cs))


