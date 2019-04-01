multThree :: (Num a) => a -> a -> a -> a 
multThree x y z = x * y * z

compareWithHundred :: (Num a, Ord a) => a -> Ordering  
compareWithHundred = compare 100  

isUpperAlphanum :: Char -> Bool 
isUpperAlphanum = (`elem` ['A'..'Z'])

zipWith' _ [] _ = []   
zipWith' _ _ [] = []   
zipWith' f (x:xs) (y:ys) = f x y : zipWith' f xs ys

flip' :: (a -> b -> c) -> (b -> a -> c)   
flip' f x y = f y x   

largestDivisible :: (Integral a) => a   
largestDivisible = head (filter p [100000,99999..])   
    where p x = x `mod` 3829 == 0

elem' :: (Eq a) => a -> [a] -> Bool   
elem' y ys = foldl (\acc x -> if x == y then True else acc) False ys

reverse' :: [a] -> [a]
reverse' x = foldl (\acc x -> x:acc) [] x
