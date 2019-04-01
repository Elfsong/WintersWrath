
factorial :: Integer -> Integer
factorial 0 = 1
factorial n | n > 0 = n * factorial(n-1) | otherwise = error "Noooo!"


myElem :: Eq a => a -> [a] -> bool
myElem _ [] = False
myElem e (x:xs) | e == x = True | otherwise = myElem e xs
