-- Bizarre example code to show how you could make a function like length
-- be treated as a number by Haskell, so you could add or multiply them.
{-# LANGUAGE FlexibleInstances #-}

module LengthNum where

instance (Foldable f, Num a) => Num (f b -> a) where
  abs x a = abs (x a)
  signum x a = signum (x a)
  fromInteger i _ = fromInteger i
  (x + y) a = (x a) + (y a)
  (x - y) a = (x a) - (y a)
  (x * y) a = (x a) * (y a)
