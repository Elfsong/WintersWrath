import qualified Data.Char as D_Char
import qualified Data.Maybe as D_Maybe
import qualified Data.List as D_List

data Pitch = Pitch { note :: Char,   
                     octave :: Char   
                   } deriving (Eq)
instance Show Pitch where
    show (Pitch note octave) = [note, octave]

data GameState = GameState { p_notes :: [Char],
                             p_octave :: [Char],
                             p_combinations :: [[[Char]]],
                             guess :: [Pitch]
                           } deriving (Eq, Show)


toPitch :: String -> Maybe Pitch
toPitch (a:b:t)
    | not (null t) = Nothing
    | (elem note' ['A'..'G']) && (elem octave' ['1'..'3']) = Just Pitch {note = a, octave = octave'}
    | otherwise = Nothing
    where note' = a
          octave' = b

feedback :: [Pitch] -> [Pitch] -> (Int,Int,Int)
feedback pitch_a pitch_b
    | (length pitch_a == 3) && (length pitch_b == 3) = (c_p, c_n - c_p, c_o - c_p)
    | otherwise = (0,0,0)
    where get_key key = foldr (\x acc -> key x:acc) []
          c_p = getCounter pitch_a pitch_b 0
          c_n = getCounter (map note pitch_a) (map note pitch_b) 0
          c_o = getCounter (map octave pitch_a) (map octave pitch_b) 0

initialGuess :: ([Pitch], GameState)
initialGuess = (currentGuess, gameState)
    where currentGuess = combinationToPitch  (all_combinations !! 0)
          gameState = GameState all_p_notes all_p_octaves all_combinations currentGuess 
          all_p_notes = "ABCDEFG"
          all_p_octaves = "123"
          all_items = getCombination all_p_notes all_p_octaves
          all_combinations = subsequencesOfSize 3 all_items
          combinationToPitch combinations = map (\(Just x) -> x) $ map toPitch combinations

-- Associated Functions 

removeItem :: (Eq a) => a -> [a] -> [a]
removeItem _ [] = []
removeItem x (y:ys) 
    | x == y = ys
    | otherwise = y : removeItem x ys 

removeMaybe :: Maybe a -> a
removeMaybe (Just x) = x

getCounter :: (Eq a) => [a] -> [a] -> Int -> Int
getCounter [] y c = c
getCounter  (x:xs) y c
    | elem x y = getCounter xs (removeItem x y) (c+1)
    | otherwise = getCounter xs y c
 
getCombination :: [a] -> [a] -> [[a]]
getCombination p_note p_octave = foldr (\x acc -> (map (\y -> y:[x]) p_note) ++ acc) [] p_octave

subsequencesOfSize :: Int -> [a] -> [[a]]
subsequencesOfSize n xs = let l = length xs
                          in if n>l then [] else subsequencesBySize xs !! (l-n)
    where subsequencesBySize [] = [[[]]]
          subsequencesBySize (x:xs) = let next = subsequencesBySize xs
                                       in zipWith (++) ([]:next) (map (map (x:)) next ++ [[]])

removeCombinations :: [Char] -> [[[Char]]] -> [[[Char]]]
removeCombinations item combinationList = currentCombination
    where currentCombination = foldr (\x acc -> if (elem item x) then acc else x:acc) [] combinationList

removeCombinationsByItem :: Char -> [[[Char]]] -> [[[Char]]]
removeCombinationsByItem item combinationList = currentCombination
    where currentCombination = foldr (\x acc -> if (subSearch item x) then acc else x:acc) [] combinationList
          subSearch item pitch = foldr (\x acc -> if (elem item  x) then True else acc) False pitch

retriveCombinations :: [Char] -> [[[Char]]] -> [[[Char]]]
retriveCombinations item combinationList = currentCombination
    where currentCombination = foldr (\x acc -> if (elem item x) then x:acc else acc) [] combinationList

retriveCombinationsByItem :: Char -> [[[Char]]] -> [[[Char]]]
retriveCombinationsByItem item combinationList = currentCombination
    where currentCombination = foldr (\x acc -> if (subSearch item x) then x:acc else acc) [] combinationList
          subSearch item pitch = foldr (\x acc -> if (elem item  x) then True else acc) False pitch













