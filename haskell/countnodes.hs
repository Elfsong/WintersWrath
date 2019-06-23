module Countnodes where

data Tree t = Leaf | Node (Tree t) t (Tree t)

countnodes :: Tree t -> Int
countnodes Leaf = 0
countnodes (Node l _ r) = (countnodes l) + 1 + (countnodes r)

x1 :: Tree Int
x1 = Node Leaf 1 Leaf
x2 :: Tree Int
x2 = Node Leaf 2 Leaf
x3 :: Tree Int
x3 = Node x1 3 x2
