module Main(main) where

show1 :: Bool -> Bool -> String

show1 True True   = "female staff"
show1 True False  = "female student"
show1 False True  = "male staff"
show1 False False = "male student"

main =
	let isFemale = True in
	let isStaff = False in
	do
		putStrLn (show1 isFemale isStaff)
