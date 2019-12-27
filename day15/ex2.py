import Processor
from Step import Step

with open('input.txt') as f:
    common_code = f.readline().strip().split(',')

computer = Processor.Processor(common_code, 0)
computer.reset()

step_tree = Step(None, (0, 0), 'O')
direction_map = [None, 2, 1, 4, 3]
oxygen_coords = (None, None)


def withdraw(direction):
    while True:
        try:
            computer.run()
        except Processor.ProcessorInputException:
            computer.push_input(direction_map[direction])
        except Processor.ProcessorOutputException:
            return


def do_step(upstream, direction):
    global oxygen_coords
    while True:
        try:
            computer.run()
        except Processor.ProcessorInputException:
            computer.push_input(direction)
        except Processor.ProcessorOutputException:
            result = computer.read_output()
            next_step = upstream.add_leaf(direction, result)
            if result != 0 and next_step:
                if result == 2:
                    oxygen_coords = next_step.coords
                for i in range(1, 5):
                    if direction_map[i] == direction:
                        continue
                    do_step(next_step, i)
                withdraw(direction)
            return


do_step(step_tree, 1)
do_step(step_tree, 2)
do_step(step_tree, 3)
do_step(step_tree, 4)

# At this point we have an unidirectional graph so several leafs may represent the same coordinates.
# For ex 2 it is convenient to reduce leafs to coordinates, which more-less will work as a map
# instead of set of paths.

adjacency_map = dict()
points = []
for terminal_leaf in step_tree.get_terminal_leafs():
    for leaf in terminal_leaf.go_upstream():
        if leaf.value != 0:
            siblings = adjacency_map.get(leaf.coords, set())
            if not siblings:
                for l in leaf.leafs:
                    siblings.add(l.coords)
            elif leaf.upstream:
                siblings.add(leaf.upstream.coords)
            adjacency_map[leaf.coords] = siblings

current_points = set([oxygen_coords])
count = 0

while True:
    next_current_points = set()
    for point in current_points:
        next_current_points = next_current_points | adjacency_map.get(point, set())
        try:
            del adjacency_map[point]
        except KeyError:
            next_current_points = next_current_points - set(point)
    if not adjacency_map:
        break
    count += 1
    current_points = next_current_points

# Remove starting point
print(count)
