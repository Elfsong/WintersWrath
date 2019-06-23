-- Boolean and int expressions, along with an interpreter for them.
-- From a lecture quiz.

-- Give these mutually recursive (and directly recursive) types:

data BoolExpr
    = BoolConst Bool
    | BoolOp BoolOp BoolExpr BoolExpr
    | CompOp CompOp IntExpr IntExpr
data IntExpr
    = IntConst Int
    | IntOp IntOp IntExpr IntExpr
    | IntIfThenElse BoolExpr IntExpr IntExpr
data BoolOp = And
data CompOp = LessThan
data IntOp = Plus | Times


-- Write functions to evaluate a BoolExpr and an IntExpr.
-- E.g., intExprValue (IntOp Times (IntConst 6) (IntConst 7)) = 42.
-- Include type declarations for your functions.

-- Sample answer:

boolExprValue :: BoolExpr -> Bool
boolExprValue (BoolConst b) = b
boolExprValue (BoolOp And e1 e2)
    = boolExprValue e1 && boolExprValue e2
boolExprValue (CompOp LessThan i1 i2)
    = intExprValue i1 < intExprValue i2


intExprValue :: IntExpr -> Int
intExprValue (IntConst i) = i
intExprValue (IntOp Plus i1 i2)
    = intExprValue i1 + intExprValue i2
intExprValue (IntOp Times i1 i2)
    = intExprValue i1 * intExprValue i2
intExprValue (IntIfThenElse b i1 i2)
    = if boolExprValue b
      then intExprValue i1
      else intExprValue i2
