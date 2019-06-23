module Derive where

data CannotShow = CannotShow
	-- deriving (Show)

-- data CannotDeriveShow = CannotDeriveShow CannotShow
-- 	deriving (Show)

data Tree k v = Leaf | Node k v (Tree k v) (Tree k v)
	deriving (Eq, Show)

showtree :: Tree k v -> String
showtree tree = show tree
