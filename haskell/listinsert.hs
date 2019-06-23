listInsert :: Ord a => a -> [a] -> [a]
listInsert elt [] = [elt]
listInsert elt (e:es)
  | e < elt   = e:listInsert elt es
  | otherwise = elt:e:es
