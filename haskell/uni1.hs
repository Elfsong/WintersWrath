module Uni1 where

show1 :: Bool -> Bool -> String

show1 True True   = "female staff"
show1 True False  = "female student"
show1 False True  = "male staff"
show1 False False = "male student"

-- let isFemale = True
-- let isStaff = False
-- show1 isFemale isStaff
-- show1 isStaff isFemale
