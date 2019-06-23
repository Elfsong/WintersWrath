-- vim: ts=4 sw=4 expandtab syntax=haskell

module Units where

data Length = Meters Double

meters_to_length :: Double -> Length
meters_to_length m = Meters m

feet_to_length :: Double -> Length
feet_to_length f = Meters (f / 0.3048)

add_lengths :: Length -> Length -> Length
add_lengths (Meters a) (Meters b) = Meters (a+b)

data Duration = Seconds Int
data Time = SecondsSinceEpoch Int

add_durations :: Duration -> Duration -> Duration
add_durations (Seconds a) (Seconds b) = Seconds (a+b)

add_duration_to_time :: Time -> Duration -> Time
add_duration_to_time (SecondsSinceEpoch sse) (Seconds t) =
    SecondsSinceEpoch (sse + t)
