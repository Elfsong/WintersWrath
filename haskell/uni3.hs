module Uni3 where

data Gender = Female | Male
	deriving (Eq, Show)

data Role = Staff | Student
	deriving (Eq, Show)

data Person = Person Gender Role
	-- deriving (Eq, Show)

show3 :: Person -> String

show3 (Person Female Staff)   = "female staff"
show3 (Person Female Student) = "female student"
show3 (Person Male Staff)     = "male staff"
show3 (Person Male Student)   = "male student"

-- show3 (Person Female Student)
