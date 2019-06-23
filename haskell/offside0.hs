zero = len []
one
 = len
      []
two = len [1,2] three = len [1,2,3]
four = len [1,
     2,3,
         4]
 len []     = 0
 len (x:xs) = 1 + len xs
