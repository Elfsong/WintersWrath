-- vim: ts=4 sw=4 expandtab syntax=haskell

module Map where

map2 :: (a -> b) -> [a] -> [b]
map2 _ [] = []
map2 f (x:xs) = (f x):(map2 f xs)

data Customer = Customer {
        customer_id         :: Int,
        customer_name       :: String,
        customer_address    :: [String]
    } deriving (Eq, Show)

get_names :: [Customer] -> [String]
get_names customers = map2 customer_name customers

cust1 = Customer 1 "Alice" ["Wonderland"]
cust2 = Customer 2 "Bobby" ["Kennedy"]
cust3 = Customer 3 "Charlie" ["Rose"]

custs = [cust1, cust2, cust3]
