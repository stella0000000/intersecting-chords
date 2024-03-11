# https://editor.p5js.org/ste11a/sketches/gCEGx_ci0

import heapq as heap

# Parse identifiers for uniformity
# Remove non-alphanumeric
def parse_id(id):
  res = "".join(filter(str.isalnum, id))
  return res

# { rad_s1: s1, rad_e1: e1, rad_s2: s2, rad_e2: e2, ...}
def populate_radians_map(input):
  radians_map = {}
  id_map = {}
  num_radians = len(input[0])

  for i in range(num_radians):
    rad, id = input[0][i], parse_id(input[1][i])
    radians_map[rad] = id
    id_map[id] = rad

  return radians_map

# { s1: rad_s1, e1: rad_e1, ...}
def populate_id_map(input):
  id_map = {}
  num_radians = len(input[0])

  for i in range(num_radians):
    rad, id = input[0][i], parse_id(input[1][i])
    id_map[id] = rad

  return id_map

# Count the number of intersections among chords within a circle
def number_of_intersections(input):
  radians_map = populate_radians_map(input)
  id_map = populate_id_map(input)
  radians = list(radians_map.keys())
  
  count = 0
  heap.heapify(radians)    # min heap of radians
  end_radians = []         # min heap of end radians
  started_chords = []      # stack of chords as they start
  
  # While we have radians to consider
  while(len(radians)):
    curr_radian = heap.heappop(radians)
    id = radians_map[curr_radian]
    dir = id[0]                     # start or end
    chord = int(id[1:])             # which chord
    
    # If we are starting a chord
    if (dir == 's'):
        end_chord = f"e{chord}"
        # append corresponding end radian to min heap
        heap.heappush(end_radians, id_map[end_chord])
        # update started chords stack
        started_chords.append(chord)
    else:
        heap.heappop(end_radians)  # ending a chord
        # how many chords started after this chord?
        # -1 for array indexing
        start_after = len(started_chords) - started_chords.index(chord) - 1
        # how many end after this chord?
        end_after = len(end_radians)
        # satisfy s1 < s2 && e1 < e2 for intersection
        curr_intersections = min(start_after, end_after)
        # add to running sum
        count += curr_intersections

  return count

inputs = [
  [
    (0.78, 1.47, 1.77, 3.92),
    ("s_1", "s_2", "e_1", "e_2")
  ],
  [
     (0.9, 1.3, 1.70, 2.92),
     ('s1','e1','s2','e2')
  ],
  [
      (0.7, 1.0, 1.7, 2.1, 2.53, 3.75, 5.0, 2.5, 4.2, 5.57),
      ('s1','s2','s3','s4','s5','e1','e2','e3','e4','e5')
  ],
  [
      (0.78, 1.47, 3.5, 3.6, 3.77, 5, 5.5, 4.75),
      ('s.122189','s.2','s.3','s.4', 'e.122189','e.2','e.3','e.4')
  ]

]

for input in inputs:
  res = number_of_intersections(input)
  print('Input: ', input)
  print('Total intersections: ', res)
  print()