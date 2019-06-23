module Library where

data LibraryItem 
  = Book       Integer String String
  | Periodical Integer String Period

data Period = Days Integer | Months Integer

title (Book       _ title _) = title
title (Periodical _ title _) = title
