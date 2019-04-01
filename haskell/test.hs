lend :: (Ord(a), Num(a)) => a -> a -> Maybe a
lend amount balance = let reserve = 100
                          newBalance = balance - amount
    in if balance < reserve
    then Nothing
    else Just newBalance

quux a = let a = "Foo"
    in a ++ "tage"
