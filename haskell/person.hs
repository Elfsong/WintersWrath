module Person where

data Date = Date Int
data PostalAddress = PostalAddress Int
data EmailAddress = EmailAddress Int
data Subject = Subject Int
data Semester = Semester Int
data Mark = Mark Int

class Person a where
    date_of_birth ::    a -> Date
    postal_address ::   a -> PostalAddress
    email_address ::    a -> EmailAddress

class (Person a) => Student a where
    year_level ::       a -> Int
    results ::          a -> [(Subject, Semester, Mark)]
    send_results ::     a -> IO ()
