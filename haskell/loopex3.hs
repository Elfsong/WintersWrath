-- vim: ts=4 sw=4 expandtab syntax=haskell

module LoopEx where

f :: [Int] -> Int
f list =
    let
        skip_init_le_zero [] = []
        skip_init_le_zero (x:xs) =
            if x <= 0 then skip_init_le_zero xs else (x:xs)
        after_skip = skip_init_le_zero list
    in
        case after_skip of
            (x:xs) ->
                let
                    target = 2 * x
                    find_first_gt (x:xs) target =
                        if x <= target then find_first_gt xs target else x
                    first_gt_target = find_first_gt xs target
                in
                    3 * first_gt_target
