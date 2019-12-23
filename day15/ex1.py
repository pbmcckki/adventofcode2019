import Processor
from Step import Step
import sys

sys.setrecursionlimit(10 ** 6)
with open('input.txt') as f:
    common_code = f.readline().strip().split(',')

computer = Processor.Processor(common_code, 0)
computer.reset()

step_tree = Step(None, (0, 0), 'O')


def withdraw(computer, direction):
    direction_map = [None, 2, 1, 4, 3]
    while True:
        try:
            computer.run()
        except Processor.ProcessorInputException:
            computer.push_input(direction_map[direction])
        except Processor.ProcessorOutputException:
            return


def do_step(computer, upstream, direction):
    direction_map = [None, 2, 1, 4, 3]
    while True:
        try:
            computer.run()
        except Processor.ProcessorInputException:
            computer.push_input(direction)
        except Processor.ProcessorOutputException:
            result = computer.read_output()
            next_step = upstream.add_leaf(direction, result)
            if result == 2:
                withdraw(computer, direction)
            if result == 1 and next_step:
                for i in range(1, 5):
                    if direction_map[i] == direction:
                        continue
                    do_step(computer, next_step, i)
                withdraw(computer, direction)
            return


do_step(computer, step_tree, 1)
do_step(computer, step_tree, 2)
do_step(computer, step_tree, 3)
do_step(computer, step_tree, 4)

print(min(x.depth for x in step_tree.search_by_value(2)) - 1)