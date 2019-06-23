-- vim: ts=4 sw=4 et ft=haskell

module Expr2 where

data Binop = Add | Sub
data Unop = Uminus

data Expr
    = Number Int
    | Variable String
    | Binop Binop Expr Expr
    | Unop Unop Expr

is_compound :: Expr -> Bool
is_compound expr =
    case expr of
        Number _ -> False
        Variable _ -> False
        _ -> True
