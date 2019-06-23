-- vim: ts=4 sw=4 expandtab syntax=haskell

module MaybeOKMonad where

data MaybeOK a = OK a | Error String deriving (Show, Eq)

instance Functor MaybeOK where
  fmap _ (Error m) = Error m
  fmap f (OK x) = OK (f x)

instance Applicative MaybeOK where
  pure = OK
  (OK f) <*> (OK v) = OK (f v)
  (OK _) <*> (Error m) = Error m
  (Error m) <*> _ = Error m

instance Monad MaybeOK  where
    (OK x) >>= k    = k x
    (Error m) >>= _ = Error m

    return          = OK
    fail            = Error

maybe_head :: [a] -> MaybeOK a
maybe_head [] = Error "head of empty list"
maybe_head (x:_) = OK x

maybe_sqrt :: Int -> MaybeOK Double
maybe_sqrt x =
    if x >= 0 then
        OK (sqrt (fromIntegral x))
    else
        Error "sqrt of negative number"

maybe_sqrt_of_head :: [Int] -> MaybeOK Double
maybe_sqrt_of_head l = maybe_head l >>= maybe_sqrt
