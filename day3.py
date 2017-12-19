import numpy as np


def part_one(target):
  # Find each corner at every layer,
  # then find the edge that the value belongs to
  length = 1
  layer = 0
  found = 0
  topLeft, topRight, bottomLeft, bottomRight = 0, 0, 0, 0
  highest_seen = 2  # first layer bottomRight is 2

  while found == 0:
    length += 2
    layer += 1

    _length = length - 1
    down = _length * _length - (layer - 1)
    topLeft = down + (length - 1) / 2
    topRight = down - (length - 1) / 2

    up = length * length - layer
    bottomLeft = up - (length - 1) / 2
    bottomRight = up + (length - 1) / 2
    print(topLeft, topRight)
    print(bottomLeft, bottomRight)

    # Analyse whether target lies in any of the range:
    if highest_seen <= target and target <= topRight:
      found = 1
      print(highest_seen, topRight)
    elif topRight <= target and target <= topLeft:
      found = 2
      print(topRight, topLeft)
    elif topRight <= target and target <= bottomLeft:
      found = 3
      print(topRight, bottomLeft)
    elif bottomLeft <= target and target <= bottomRight:
      found = 4
      print(bottomLeft, bottomRight)

    if found > 0:
      print "steps so far: ", layer
      print "sides #", found
      break
    else:
      highest_seen = bottomRight

  # Traverse in the direction that gives the score, going up and down first
  if found == 1:  # RIGHT
    middle = topRight - (length - 1) / 2
    remaining = abs(target - middle)
  elif found == 2:  # UP
    remaining = abs(target - down)
  elif found == 3:  # LEFT
    middle = bottomLeft - (length - 1) / 2
    remaining = abs(target - middle)
  elif found == 4:  # DOWN
    remaining = abs(target - up)
  total = layer + remaining
  return total


def generate_moves(layer):
  current_layer = 0
  moves = []
  length = 1
  while current_layer < layer:
    length += 2
    current_layer += 1

    # moves left first
    moves.append('R')
    if current_layer == 1:
      moves.extend(['U'] * ((length - 1) / 2))
    else:
      moves.extend(['U'] * ((length - 2)))
    moves.extend(['L'] * (length - 1))
    moves.extend(['D'] * (length - 1))
    moves.extend(['R'] * (length - 1))
  return moves


def part_two(target):
  layer = target
  moves = generate_moves(layer-1)
  moves.reverse()
  print moves

  length = 1
  i = 1
  while i < layer:
    i += 1
    length += 2
  print "length", length
  store = np.zeros((length + 2, length + 2)) # Extra padding

  row = ((length - 1) / 2) + 1
  col = ((length - 1) / 2) + 1
  store[row, col] = 1
  print store
  print(row, col)

  while len(moves):
    m = moves.pop()
    if m == 'L':
      col -= 1
    elif m == 'R':
      col = col + 1
    elif m == 'U':
      row -= 1
    elif m == 'D':
      row += 1
    store[row, col] = \
        store[row - 1, col] + store[row + 1, col] + \
        store[row, col + 1] + store[row, col - 1] + \
        store[row - 1, col - 1] + store[row + 1, col + 1] + \
        store[row + 1, col - 1] + store[row - 1, col + 1]
    print moves
    print(m, row, col)
    # print store
  return store

if __name__ == "__main__":
  # s = part_one(347991)
  # print "Total number of steps taken ", str(s)

  # s = part_two(27)
  m = part_two(5)
  print np.int64(m)
  print np.min(m[m>=347991])
