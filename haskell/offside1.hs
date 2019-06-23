zero = len []
one
 = len
      []
two = len [1,2]
three = len [1,2,3]	-- has to be on new line
four = len [1,
     2,3,
         4]
len []     = 0		-- has to start in col 0
len (x:xs) = 1 + len xs	-- has to start in col 0
