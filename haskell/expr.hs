-- vim: ts=4 sw=4 et ft=haskell

module Expr where

data Binop = Add | Sub
data Unop = Uminus

data Expr
    = Number Int
    | Variable String
    | Binop Binop Expr Expr
    | Unop Unop Expr

is_static :: Expr -> Bool
is_static expr =
    case expr of
        Number n -> True
        Variable v -> False
        Unop unop expr1 -> is_static expr1
        Binop binop expr1 expr2 ->
            is_static expr1 && is_static expr2

