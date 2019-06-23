-- vim: ts=4 sw=4 expandtab syntax=haskell

module LoopEx where

skip_init_le_zero :: [Int] -> [Int]
skip_init_le_zero [] = []
skip_init_le_zero (x:xs) =
    if x <= 0 then skip_init_le_zero xs else (x:xs)

find_first_gt_target :: [Int] -> Int -> Maybe Int
find_first_gt_target [] _ = Nothing
find_first_gt_target (x:xs) target =
    if x <= target then find_first_gt_target xs target else Just x

f :: [Int] -> Maybe Int
f list =
    let skipped_init_le_zero = skip_init_le_zero list in
    case skipped_init_le_zero of
        [] -> Nothing
        (x:xs) ->
            let target = 2 * x in
            let maybe_first_gt_target = find_first_gt_target xs target in
            case maybe_first_gt_target of
                Nothing -> Nothing
                Just first_gt_target -> Just (3 * first_gt_target)
