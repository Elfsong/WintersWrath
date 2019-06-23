module TicTacToe where

data SquareContent = X | O | Empty

data TicTacToeBoard =
  TicTacToeBoard 
  SquareContent SquareContent SquareContent
  SquareContent SquareContent SquareContent
  SquareContent SquareContent SquareContent
