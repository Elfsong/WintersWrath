module Type where

data T =
	C1 Int | 
	C2 String String |
	C3 Bool Int Double
	deriving Show

kind :: T -> String
kind (C1 _) = "C1"
kind (C2 s1 s2) = "C2 " ++ s1 ++ " " ++ s2
kind (C3 _ _ _) = "C3"
