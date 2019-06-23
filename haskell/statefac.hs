-- vim: ts=4 sw=4 et ft=haskell
-- File     : statefac.hs
-- RCS      : $Id$
-- Author   : Lee Naish
-- Origin   : Mon Apr  2 11:53:18 EST 2012
-- Purpose  : Illustrate use of the Haskell State monad
-- Inspiration  : http://www.willamette.edu/~fruehr/haskell/evolution.html

module Statefac where

import Control.Monad.State

fac :: Int -> Int
fac n = snd (runState (fac' n) 1)

-- returns () but updates state
fac' :: Int -> State Int ()
fac' n =
    if n <= 0 then
        return ()
    else do
        acc <- get
        put (n * acc)
        fac' (n-1)
        return ()
