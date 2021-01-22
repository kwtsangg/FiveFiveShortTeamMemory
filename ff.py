import numpy as np
import random
import time
import gui_pygame as gui


def getDistinctRandom(N, RangeMax = [1,25]):
  return random.sample(range(RangeMax[0], RangeMax[1]), N);

def getDistinctCoordinates(N, Size = [5,5]):
  tmp_result = getDistinctRandom(N, [0, Size[0]*Size[1]])
  result = []
  for i in range(N):
    result.append( [tmp_result[i] // Size[0], tmp_result[i] % Size[1] ] )
  return result

def main():
  Size = [5,5]
  DisplayTime = 0.5
  NGamePerLevel = 10
  Board = gui.Board_gui(Size[0], Size[1])
  EmptyState = np.zeros(Size[0]*Size[1]).reshape(Size[0], Size[1])
  State = np.zeros(Size[0]*Size[1]).reshape(Size[0], Size[1])
  while 1:
    State = np.round(np.random.rand(Size[0], Size[1]))
    guess_state = np.zeros(Size[0]*Size[1]).reshape(Size[0], Size[1])
    Board.draw_board()
    Board.draw_stones(State, draw_empty = True)
    time.sleep(DisplayTime)
    Board.draw_stones(EmptyState, draw_empty = True)
    while 1:
      guess_state, is_finished = Board.asking_for_move(guess_state)
      Board.draw_stones(guess_state, draw_empty = True)
      if is_finished:
          break
    Board.draw_stones(State, color="red", radius=0.8, draw_empty = False)
    Board.freeze()

if __name__ == '__main__':
  main()
