-- vim: ts=4 sw=4 expandtab syntax=haskell

module Primes where

all_primes :: [Integer]
all_primes = prime_filter [2..]

prime_filter :: [Integer] -> [Integer]
prime_filter [] = []
prime_filter (x:xs) = x:prime_filter (filter (not . (`divisibleBy` x)) xs)

-- n `divisibleBy` d means n is evenly divisible by d
divisibleBy n d = n `mod` d == 0

-- The first n primes:
--    take n all_primes

-- All the primes up to n:
--    takeWhile (<= n) all_primes
