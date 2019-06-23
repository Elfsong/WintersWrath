-- sumlist :: [Int] -> Int
-- sumlist [] = 0
-- sumlist (x:xs) = x + sumlist xs

-- iota' :: Int -> [Int]
-- iota' n = if n == 0 then [] else iota' (n-1) ++ [n]

-- len' :: [a] -> Int
-- len' [] = 0
-- len' (x:xs) = 1 + len' xs

-- show1 :: Bool -> Bool -> String
-- -- intended usage: show1 isFemale isStaff 
-- show1 True True = "female staff"
-- show1 True False = "female student" 
-- show1 False True = "male staff"
-- show1 False False = "male student"

-- data Gender = Female | Male 
-- data Role = Staff | Student

-- show2 :: Gender -> Role -> String
-- show2 Female Staff = "female staff"
-- show2 Female Student = "female student" 
-- show2 Male Staff = "male staff"
-- show2 Male Student = "male student"

-- data Suit = Club | Diamond | Heart | Spade deriving Show
-- data Rank = R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | Jack | Queen | King | Ace deriving Show
-- data Card = Card Suit Rank deriving Show

-- a = Card Club R2
-- Card x y = a

-- nonNegElts :: (Ord a, Num a) => [a] -> [a]
-- nonNegElts [] = []
-- nonNegElts (x:xs)
--     | x >= 0 = x:nonNegElts xs
--     | otherwise = nonNegElts xs

-- subLists :: [a] -> [[a]]
-- subLists [] = [[]]
-- subLists (x:xs) = (addToEach x restSeqs) ++ (restSeqs)
--     where restSeqs = subLists xs

-- addToEach :: a -> [[a]] -> [[a]]
-- addToEach h [] = []
-- addToEach h (r:rs) = (h:r):(addToEach h rs)

-- listInsert :: (Ord a) => a -> [a] -> [a]
-- listInsert elem [] = [elem]
-- listInsert elem (x:xs)
--     | elem > x = x:(listInsert elem xs)
--     | otherwise = elem:x:xs

-- filter' :: (a -> Bool) -> [a] -> [a]
-- filter' _ [] = []
-- filter' f (x:xs)
--     | f x = x:(filter' f xs)
--     | otherwise = filter' f xs

-- is_long :: String -> Bool
-- is_long s = if (len' s >= 3) then True else False

-- is_even :: Int -> Bool
-- is_even x = (x `mod` 2 == 0)

-- suml :: Num a => [a] -> a 
-- suml = foldl (+) 0

-- concatr :: [[a]] -> [a]
-- concatr = foldr (++) []

-- flip' :: [a] -> [a]
-- flip' [] = []
-- flip' (x:xs)= flip' xs ++ [x]

-- reverseList' x = foldl (\acc x -> x : acc) x

-- maxList' x = foldl (\acc x -> if x > acc then x else acc) 0 x

-- qs2 [] = []
-- qs2 (x:xs) = qs2 littles ++ [x] ++ qs2 bigs
--     where littles = [l | l <- xs, l < x] 
--           bigs =[b | b <- xs, b >= x]


-- pairs = [(a, b) | a <- [1, 2, 3], b <- [1, 2, 3]]
-- pairs = [(a, b) | a <- [1, 2, 3], b <- [1, 2, 3], a + b <= 5]

-- countDown :: Int -> IO ()
-- countDown n
--     | n == 0 = do
--         putStrLn "Done."
--     | otherwise = do
--         print n
--         countDown $ n - 1

-- readlen :: IO Int
-- readlen = do
--     str <- getLine 
--     return (length str)

-- foldr' :: (e -> v -> v) -> v -> [e] -> v 
-- -- foldr :: Foldable t => (a -> b -> b) -> b -> t a -> b
-- foldr' _ base [] = base
-- foldr' f base (x:xs) = f x $ foldr' f base xs

-- divide_list :: Int-> [a]->([a],[a])
-- divide_list _ [] =([],[])
-- divide_list n (x:xs)
--      | n==0 =([],x:xs)
--      | otherwise =
--          let (half1,half2)=
--              divide_list (n-1) xs
--          in 
--              (x:half1, half2)

-- balanced_fold :: (e -> e -> e) -> e -> [e] -> e
-- balanced_fold _ b []  = b
-- balanced_fold f b [a] = f b a
-- balanced_fold f b l =
--    let len= length l
--        (half1,half2)= divide_list (div len 2) l
--        value1=balanced_fold f b half1
--        value2=balanced_fold f b half2
--    in f value1 value2

-- xor :: Bool -> Bool -> Bool
-- xor x y = if x /= y then True else False

-- myAppend :: [a] -> [a] -> [a]
-- myAppend x y = x ++ y

-- myReverse :: [a] -> [a]
-- myReverse [] = []
-- myReverse (x:xs) = (myReverse xs) ++ [x]

-- getNthElem :: Int -> [a] -> a
-- getNthElem _ [] = error "Error"
-- getNthElem n (l:ls)
--     | n > 0 = getNthElem (n-1) ls
--     | otherwise = l

-- type Font_tag = [Font_specifier]

-- data Font_color = Colour_name String
--                 | Hex Int
--                 | RGB Int Int Int

-- data Font_specifier = Font_size Int
--                     | Font_face String
--                     | Font_color Font_color

-- factorial :: Int -> Int
-- factorial 0 = 1
-- factorial x = x * factorial (x-1)

-- myElem :: (Eq a) => a -> [a] -> Bool
-- myElem _ [] = False
-- myElem n (l:ls)
--     | n == l = True
--     | otherwise = myElem n ls

-- longestPrefix :: String -> String -> String
-- longestPrefix "" _ = ""
-- longestPrefix _ "" = ""
-- longestPrefix (x:xs) (y:ys) 
--     | x == y = [x] ++ (longestPrefix xs ys)
--     |otherwise = longestPrefix xs ys

-- listRange1 :: Int -> Int -> [Int]
-- listRange1 x y = [x..y]

-- listRange2 :: Int -> Int -> [Int]
-- listRange2 x y
--     | x > y = error "x should smaller then y"
--     | x < y = x:listRange2 (x+1) y
--     | otherwise = [y]

-- ftoc :: Double -> Double
-- ftoc f = (5/9) * (f - 32)

-- merge :: Ord a => [a] -> [a] -> [a]
-- merge [] x = x
-- merge x [] = x
-- merge (x:xs) (y:ys)
--     | x < y = x:(merge xs (y:ys))
--     | otherwise = y:(merge (x:xs) ys)

-- quicksort :: Ord a => [a] -> [a]
-- quicksort [] = []
-- quicksort (x:xs) = quicksort leftList ++ [x] ++ quicksort rightList
--     where   leftList = filter (<x) xs
--             rightList = filter (>=x) xs 

-- data Expression = 
--     Var Variable
--     | Num Integer
--     | Plus Expression Expression
--     | Minus Expression Expression
--     | Times Expression Expression
--     | Div Expression Expression

-- data Variable = A | B

-- eval a b (Var A) = a
-- eval a b (Var B) = b
-- eval a b (Num n) = n
-- eval a b (Plus  e1 e2) = (eval a b e1) + (eval a b e2)
-- eval a b (Minus e1 e2) = (eval a b e1) - (eval a b e2)
-- eval a b (Times e1 e2) = (eval a b e1) * (eval a b e2)
-- eval a b (Div   e1 e2) = (eval a b e1) `div` (eval a b e2)

-- exp1 = Plus (Times (Num 2) (Var A)) (Var B)

-- data Tree a = Empty | Node (Tree a) a (Tree a)

-- treesort :: Ord a => [a] -> [a]
-- treesort x = tree_to_list (list_to_bst x)

-- tree_to_list :: Tree a -> [a]
-- tree_to_list Empty = []
-- tree_to_list (Node leftTree value rightTree) = tree_to_list leftTree ++ [value] ++ tree_to_list rightTree

-- list_to_bst :: Ord a => [a] -> Tree a
-- list_to_bst [] = Empty
-- list_to_bst (x:xs) = bst_insert x (list_to_bst xs)

-- bst_insert :: Ord a => a  -> Tree a -> Tree a
-- bst_insert i Empty = Node Empty i Empty
-- bst_insert i (Node l v r)
--     | i <= v = (Node (bst_insert i l) v r)
--     | i  > v = (Node l v (bst_insert i r))

-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% --
-- data Tree a = Empty | Node (Tree a) a (Tree a)

-- treeSort :: Ord a => [a] -> [a]
-- treeSort x = tree2list $ list2bst x

-- tree2list :: Tree a -> [a]
-- tree2list Empty = []
-- tree2list (Node l v r) = (tree2list l) ++ [v] ++ (tree2list r)

-- list2bst :: Ord a => [a] -> Tree a
-- list2bst [] = Empty
-- list2bst (l:ls) = bstInsert l $ list2bst ls

-- bstInsert :: Ord a => a -> Tree a -> Tree a
-- bstInsert x Empty = Node Empty x Empty
-- bstInsert x (Node l v r)
--     | x >= v = (Node l v (bstInsert x r))
--     | x <  v = (Node (bstInsert x l) v r)


-- transpose :: [[a]] -> [[a]]
-- transpose [] = []
-- transpose o
--     | length (head o) == 0 = [] 
--     | otherwise = [head'] ++ (transpose tail')
--         where   head' = map head o
--                 tail' = map tail o

-- triple :: (Num a, Foldable t) => t a -> (a, a, a)
-- triple x = (length', sum', sum_square')
--     where   length' = foldl (\acc x -> acc + 1) 0 x
--             sum' = foldl (\acc x -> acc + x) 0 x
--             sum_square' = foldl (\acc x -> acc + x * x) 0 x

-- maybeApply :: (a -> b) -> Maybe a -> Maybe b
-- maybeApply f Nothing = Nothing
-- maybeApply f (Just x) = Just(f x)

-- zWith :: (a -> b -> c) -> [a] -> [b] -> [c]
-- zWith f [] _ = []
-- zWith f (x:xs) (y:ys) = (f x y):(zWith f xs ys)

-- linearEqn :: Num a => a -> a -> [a] -> [a]
-- linearEqn a b [] = [] 
-- linearEqn a b (x:xs) = (a * x + 1) : (linearEqn a b xs)

-- sqrtPM :: (Floating a, Ord a) => a -> [a]
-- sqrtPM x
--     | x == 0 = [0]
--     | x > 0 = let r = sqrt x in [r, -r]
--     | otherwise = []

-- allSqrts :: (Floating a, Ord a) => [a] -> [a]
-- allSqrts [] = []
-- allSqrts (x:xs) = sqrtPM x ++ (allSqrts xs)

-- filter' :: (a -> Bool) -> [a] -> [a]
-- filter' f [] = []
-- filter' f (x:xs)
--     | f x       = x:(filter' f xs)
--     | otherwise = filter' f xs

-- map' :: (a -> b) -> [a] -> [b]
-- map' f [] = []
-- map' f (x:xs) = (f x):(map' f xs) 
