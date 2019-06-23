-- vim: ts=4 sw=4 et ft=haskell
-- File     : monadexample.hs
-- RCS      : $Id$
-- Author   : Peter Schachte
-- Origin   : Wed Oct 13 21:43:11 2010
-- Purpose  : Illustrate use of the Haskell State monad

module Statemonad where

import Control.Monad.State

data Tree a = Empty | Node (Tree a) a (Tree a) deriving Show
type IntTree = Tree Int

testTree :: IntTree
testTree = Node (Node Empty 10 Empty) 20 (Node Empty 30 (Node Empty 40 Empty))

----------------------------------------------------------------

incTree :: IntTree -> IntTree
incTree Empty = Empty
incTree (Node l e r) = 
    Node (incTree l) (e + 1) (incTree r)

----------------------------------------------------------------

incTree1 :: IntTree -> IntTree
incTree1 tree = fst (incTree1' tree 1)

incTree1' :: IntTree -> Int -> (IntTree, Int)
incTree1' Empty n = (Empty, n)
incTree1' (Node l e r) n =
    let (newl, n1) = incTree1' l n
        (newr, n2) = incTree1' r (n1 + 1)
    in  (Node newl (e+n1) newr, n2)

----------------------------------------------------------------

incTree2 :: IntTree -> IntTree
incTree2 tree = fst (runState (incTree2' tree) 1)

incTree2' :: IntTree -> State Int IntTree
incTree2' Empty = return Empty
incTree2' (Node l e r) = do
    newl <- incTree2' l
    n <- get
    put (n + 1)
    newr <- incTree2' r
    return (Node newl (e+n) newr)

----------------------------------------------------------------

type Counter = State Int

withCounter :: Int -> Counter a -> a
withCounter init f = fst (runState f init)

nextCount :: Counter Int
nextCount = do
    n <- get
    put (n + 1)
    return n

incTree3 :: IntTree -> IntTree
incTree3 tree = withCounter 1 (incTree3' tree)

incTree3' :: IntTree -> Counter IntTree
incTree3' Empty = return Empty
incTree3' (Node l e r) = do 
    newl <- incTree3' l
    n <- nextCount
    newr <- incTree3' r
    return (Node newl (e+n) newr)

----------------------------------------------------------------
