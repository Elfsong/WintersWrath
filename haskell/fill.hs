-- Haskell function to fill a paragraph taking words from a supplied list.  
-- Inputs are the width of the paragraph and a list of words; result is a 
-- list of lines.

fill :: Int -> [String] -> [String]
fill _ [] = []
fill width (w:ws) =
  let (line,residue) = fillLine (width-length w) ws
  in  (w++line):fill width residue

fillLine :: Int -> [String] -> (String,[String])
fillLine width [] = ("",[])
fillLine width (w:ws) =
  let width' = width - length w - 1
  in  if width' >= 0
      then let (line,residue) = fillLine width' ws
           in  (' ':w++line,residue)
      else ("",w:ws)
