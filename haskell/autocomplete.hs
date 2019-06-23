-- vim: ts=4 sw=4 expandtab syntax=haskell

module Autocomplete where

import Data.Map
import Data.Set

data WindowId = WindowId Int deriving (Eq, Ord)
data ProgState = ProgState Int deriving (Eq, Ord)

type SourceMap = Map WindowId [ProgState -> Set String]

get_sources :: ProgState -> SourceMap -> WindowId -> Set String
get_sources ps source_map window_id =
    let
        maybe_source_funcs = Data.Map.lookup window_id source_map
    in
        case maybe_source_funcs of
            Nothing ->
                Data.Set.empty
            Just source_funcs ->
                let sources = apply_prog_state ps source_funcs in
                union_list sources

apply_prog_state :: ProgState -> [ProgState -> a] -> [a]
apply_prog_state _ [] = []
apply_prog_state ps (f:fs) = (f ps):(apply_prog_state ps fs)

union_list :: Ord a => [Set a] -> Set a
union_list [] = Data.Set.empty
union_list (s:ss) = Data.Set.union s (union_list ss)
