input = """0 5 10 0 11 14 13 4 11 8 8 7 1 4 12 11"""
import numpy as np


def part_one():
  # input = "0 2 7 0"
  states = []
  banks = {}
  for i, b in enumerate(input.split()):
    banks[i] = int(b)
  print banks
  num_bank = len(banks.values())

  num_step = 0
  while True:
    currentState = banks.values()
    print currentState

    if currentState in states:
      states.append(currentState)
      break
    states.append(currentState)
    num_step += 1

    idx = np.argmax(currentState)
    val = banks[idx]
    banks[idx] = 0
    rounds = val / num_bank
    remainder = val % num_bank
    # print(val, rounds, remainder)

    for i in range(num_bank):
      banks[i] += rounds
    # add the remainder
    _idx = idx
    while _idx < num_bank and remainder > 0:

      _idx += 1
      if _idx == num_bank:
        _idx = 0
      banks[_idx] += 1
      remainder -= 1
  return states

def part_two():
  states = part_one()
  print "\n\n"
  first = False
  last = [10, 9, 8, 7, 6, 5, 4, 3, 1, 1, 0, 15, 14, 13, 11, 12]
  idx = 0
  count = 0
  while True:
    print idx, states[idx]

    if states[idx] == last:
      print "found"
      if first:
        break
      else:
        first = True
        count = 0
        print 'First'

    idx += 1
    count += 1

  return count

if __name__ == "__main__":
  # print part_one()[-1]
  print part_two()
