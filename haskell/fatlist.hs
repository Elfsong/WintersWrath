-- vim: ts=4 sw=4 expandtab syntax=haskell
{-# OPTIONS_GHC -XMultiParamTypeClasses -XFlexibleInstances #-}
module FatList where

data FatList a
    = FCons0 (FatRest a)
    | FCons1 a (FatRest a)
    | FCons2 a a (FatRest a)
    deriving (Show, Eq)

data FatRest a
    = FatNil
    | FatRest a a a (FatRest a)
    deriving (Show, Eq)


toFatList :: [a] -> FatList a
toFatList (x1:x2:x3:xt) = fcons3 x1 x2 x3 (toFatList xt)
toFatList [x1,x2]       = FCons2 x1 x2 FatNil
toFatList [x1]          = FCons1 x1 FatNil
toFatList []            = FCons0 FatNil

fcons3 :: a -> a -> a -> FatList a -> FatList a
fcons3 e1 e2 e3 (FCons0 fr)
  = FCons0 (FatRest e1 e2 e3 fr)
fcons3 e1 e2 e3 (FCons1 e4 fr)
  = FCons1 e1 $ FatRest e2 e3 e4 fr
fcons3 e1 e2 e3 (FCons2 e4 e5 fr)
  = FCons2 e1 e2 $ FatRest e3 e4 e5 fr


fromFatList :: FatList a -> [a]
fromFatList (FCons0 fr) = fromFatList' fr
fromFatList (FCons1 x1 fr) = x1:fromFatList' fr
fromFatList (FCons2 x1 x2 fr) = x1:x2:fromFatList' fr

fromFatList' :: FatRest a -> [a]
fromFatList' FatNil                = []
fromFatList' (FatRest e1 e2 e3 fr) = e1:e2:e3:fromFatList' fr


fatLength :: FatList a -> Int
fatLength (FCons0 fr)       =     fatLength' fr
fatLength (FCons1 x1 fr)    = 1 + fatLength' fr
fatLength (FCons2 x1 x2 fr) = 2 + fatLength' fr

fatLength' :: FatRest a -> Int
fatLength' FatNil                = 0
fatLength' (FatRest e1 e2 e3 fr) = 3 + fatLength' fr


fatAppend :: FatList a -> FatList a -> FatList a
fatAppend (FCons0 xr) ys
  = fatAppend' xr ys
fatAppend (FCons1 x1 xr) ys
  = fcons x1 $ fatAppend' xr ys
fatAppend (FCons2 x1 x2 xr) ys
  = fcons x1 $ fcons x2 $ fatAppend' xr ys

fatAppend' FatNil ys = ys
fatAppend' (FatRest x1 x2 x3 xr) ys
  = fcons3 x1 x2 x3 $ fatAppend' xr ys

fcons :: a -> FatList a -> FatList a
fcons x1 (FCons0 xr)       = FCons1 x1 xr
fcons x1 (FCons1 x2 xr)    = FCons2 x1 x2 xr
fcons x1 (FCons2 x2 x3 xr) = FCons0 $ FatRest x1 x2 x3 xr


class List l a where
  nil      :: l a
  cons     :: a -> l a -> l a
  car      :: l a -> a
  cdr      :: l a -> l a
  len      :: l a -> Int
  append   :: l a -> l a -> l a
  fromList :: [a] -> l a
  toList   :: l a -> [a]

instance List FatList a where
  nil      = FCons0 FatNil
  cons     = fcons
  len      = fatLength
  append   = fatAppend
  fromList = toFatList
  toList   = fromFatList

  car (FCons0 (FatRest x1 _ _ _)) = x1
  car (FCons1 x1 _)               = x1
  car (FCons2 x1 _ _)             = x1

  cdr (FCons0 (FatRest _ x1 x2 xr)) = FCons2 x1 x2 xr
  cdr (FCons1 _ xr)                 = FCons0 xr
  cdr (FCons2 _ x1 xr)              = FCons1 x1 xr

instance List [] a where
  nil      = []
  cons     = (:)
  len      = length
  append   = (++)
  fromList = id
  toList   = id
  car      = head
  cdr      = tail
