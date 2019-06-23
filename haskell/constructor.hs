-- vim: ts=4 sw=4 expandtab syntax=haskell

module Constructor where

data BST a
    = Empty
    | Node (BST a) a (BST a)

class Collection c a where
    size ::   c a -> Int
    empty ::  c a
    cons ::   a -> c a -> c a

instance Collection [] a where
    size =  length
    empty = []
    cons =  (:)

instance Ord a => Collection BST a where
    size =  count_items_bst
    empty = empty_bst
    cons =  insert_bst

count_items_bst :: BST a -> Int
count_items_bst Empty = 0
count_items_bst (Node l _ r) =
    count_items_bst l + count_items_bst r

empty_bst :: BST a
empty_bst = Empty

insert_bst :: (Ord a) => a -> BST a -> BST a
insert_bst x Empty = Node Empty x Empty
insert_bst x (Node l i r)
    | x < i = Node (insert_bst x l) i r
    | x > i = Node l i (insert_bst x r)
    | otherwise = Node l x r
