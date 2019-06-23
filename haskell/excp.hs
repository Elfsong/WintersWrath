-- vim: ts=4 sw=4 expandtab syntax=haskell

module Excp where

map2 :: (a -> b) -> [a] -> [b]
map2 _ [] = []
map2 f (x:xs) = (f x):(map2 f xs)

data Customer
    = Customer {
        customer_id      :: Int,
        customer_name    :: String,
        customer_address :: [String]
      }
    | AnonCustomer {
        anon_id          :: Int,
        anon_po_box      :: [String]
      }
    deriving (Eq, Show)

get_names :: [Customer] -> [String]
-- get_names customers = map2 customer_name customers
get_names = map2 customer_name

cust1 = Customer 1 "Alice" ["Wonderland"]
cust2 = Customer 2 "Bobby" ["Kennedy"]
cust3 = Customer 3 "Charlie" ["Rose"]
cust4 = AnonCustomer 4 ["box 1"]

custs3 = [cust1, cust2, cust3]
custs4 = [cust1, cust2, cust3, cust4]
