-- Make an acronym from a phrase
-- Eg:  acronym "self contained underwater breathing apparatus" == "scuba"

acronym :: String -> String
acronym [] = []
acronym (l:ls) = l:acronym (skipPastSpace ls)

skipPastSpace :: String -> String
skipPastSpace [] = []
skipPastSpace (' ':rest) = skipSpaces rest
skipPastSpace (_:rest) = skipPastSpace rest

skipSpaces :: String -> String
skipSpaces [] = []
skipSpaces (' ':rest) = skipSpaces rest
skipSpaces rest = rest
