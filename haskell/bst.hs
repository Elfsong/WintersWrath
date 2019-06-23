module BST where

data Tree k v = Leaf | Node k v (Tree k v) (Tree k v)
        deriving (Eq, Show)

countnodes :: Tree k v -> Int
countnodes Leaf = 0
countnodes (Node _ _ l r) = 1 + (countnodes l) + (countnodes r)

search_bst :: Ord k => Tree k v -> k -> Maybe v
search_bst Leaf _ = Nothing
search_bst (Node k v l r) sk =
    if k == sk then
        Just v
    else if sk < k then
        search_bst l sk
    else
        search_bst r sk

-- The same code, but prettier
search_bst2 :: Ord k => Tree k v -> k -> Maybe v
search_bst2 Leaf _ = Nothing
search_bst2 (Node k v l r) sk
  | sk == k   = Just v
  | sk <  k   = search_bst2 l sk
  | otherwise = search_bst2 r sk

insert_bst :: Ord k => Tree k v -> k -> v -> Tree k v
insert_bst Leaf ik iv = Node ik iv Leaf Leaf
insert_bst (Node k v l r) ik iv =
    if k == ik then
        Node ik iv l r
    else if ik < k then
        Node k v (insert_bst l ik iv) r
    else
        Node k v l (insert_bst r ik iv)

assoc_list_to_bst :: Ord k => [(k, v)] -> Tree k v
assoc_list_to_bst [] = Leaf
assoc_list_to_bst ((hk, hv):kvs) =
    let t0 = assoc_list_to_bst kvs
    in  insert_bst t0 hk hv

assoc_list_to_bst2 :: Ord k => [(k, v)] -> Tree k v
assoc_list_to_bst2 [] = Leaf
assoc_list_to_bst2 ((hk, hv):kvs) = insert_bst t0 hk hv
    where t0 = assoc_list_to_bst2 kvs
