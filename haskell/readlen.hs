module ReadLen where

main :: IO ()
main = do
	len <- readlen
	putStrLn $ "The length of that string is " ++ show len

readlen :: IO Int
readlen = do
	putStrLn "Please input a string"
	str <- getLine
	return (length str)
