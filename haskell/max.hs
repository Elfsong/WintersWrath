-- vim: ts=4 sw=4 expandtab syntax=haskell

module Max where

data RepType1 = Rep1 [Int]
data RepType2 = Rep2 Int [Int]

max_rep1 :: RepType1 -> Int
max_rep1 item_list =
    case item_list of
        Rep1 [] -> error "empty item_list"
        Rep1 (head:tail) -> foldr max head tail

max_rep2 :: RepType2 -> Int
max_rep2 item_list =
    let Rep2 head tail = item_list in
    foldr max head tail
