module Uni2 where

data Gender = Female | Male
	deriving (Eq, Show)

data Role = Staff | Student
	deriving (Eq, Show)

show2 :: Gender -> Role -> String

show2 Female Staff   = "female staff"
show2 Female Student = "female student"
show2 Male Staff     = "male staff"
show2 Male Student   = "male student"

-- let gender = Female
-- let role = Student
-- show2 gender role
-- show2 role gender
