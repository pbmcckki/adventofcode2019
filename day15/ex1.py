import Processor
from Step import Step

with open('input.txt') as f:
    common_code = f.readline().strip().split(',')

computer = Processor.Processor(common_code, 0)
computer.reset()

step_tree = Step(None, (0, 0), 'O')
direction_map = [None, 2, 1, 4, 3]


def withdraw(direction):
    while True:
        try:
            computer.run()
        except Processor.ProcessorInputException:
            computer.push_input(direction_map[direction])
        except Processor.ProcessorOutputException:
            return


def do_step(upstream, direction):
    while True:
        try:
            computer.run()
        except Processor.ProcessorInputException:
            computer.push_input(direction)
        except Processor.ProcessorOutputException:
            result = computer.read_output()
            next_step = upstream.add_leaf(direction, result)
            # We are at the oxygen station, no need to go further
            if result == 2:
                withdraw(direction)
            # We have clear way and no loop on current path
            if result == 1 and next_step:
                for i in range(1, 5):
                    # Do not try to go back, push forward :)
                    if direction_map[i] == direction:
                        continue
                    do_step(next_step, i)
                withdraw(direction)
            return


do_step(step_tree, 1)
do_step(step_tree, 2)
do_step(step_tree, 3)
do_step(step_tree, 4)

# Subtract -1 for root node, it does not count as a step
print(min(x.depth for x in step_tree.search_by_value(2)) - 1)
