module Hello where

hello :: IO ()
hello = do
	putStr $ "Hello, "
	putStrLn $ "world"
