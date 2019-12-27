import Processor
from Step import Step

with open('input.txt') as f:
    common_code = f.readline().strip().split(',')

computer = Processor.Processor(common_code, 0)
computer.reset()

step_tree = Step(None, (0, 0), 'O')
direction_map = [None, 2, 1, 4, 3]
min_x, min_y, max_x, max_y = 0, 0, 0, 0


def withdraw(direction):
    while True:
        try:
            computer.run()
        except Processor.ProcessorInputException:
            computer.push_input(direction_map[direction])
        except Processor.ProcessorOutputException:
            return


def do_step(upstream, direction):
    global oxygen_position, min_x, min_y, max_x, max_y
    while True:
        try:
            computer.run()
        except Processor.ProcessorInputException:
            computer.push_input(direction)
        except Processor.ProcessorOutputException:
            result = computer.read_output()
            next_step = upstream.add_leaf(direction, result)
            if next_step.coords[0] > max_x:
                max_x = next_step.coords[0]
            if next_step.coords[0] < min_x:
                min_x = next_step.coords[0]
            if next_step.coords[1] > max_y:
                max_y = next_step.coords[1]
            if next_step.coords[1] < min_y:
                min_y = next_step.coords[1]
            if result != 0 and next_step:
                if result == 2:
                    oxygen_position = upstream.coords
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

print(oxygen_position)
print(min_x,min_y,max_x,max_y)