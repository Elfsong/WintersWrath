countDown :: Int -> IO ()
countDown n
  | n < 0 = putStrLn "Done."
  | otherwise = do
    print n
    countDown $ n - 1

countDown2 :: Int -> IO ()
countDown2 n = do
  if n < 0 then do
    putStrLn "Done."
  else do
    print n
    countDown2 $ n - 1

countDown3 :: Int -> IO ()
countDown3 n =
  if n < 0 then
    putStrLn "Done."
  else do
    print n
    countDown3 $ n - 1