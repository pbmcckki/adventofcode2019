from Processor import Processor, ProcessorEndOfProgramException
from itertools import permutations

with open('input.txt') as f:
    common_code = f.readline().strip().split(',')

common_code = [str(x) for x in common_code]

computer = [Processor(common_code,i) for i in range(0, 5)]
max_vector = None
max_output = 0
for input_vector in permutations(range(0, 5)):
    # initialize
    for i in range(0, 5):
        computer[i].reset()
        computer[i].run()
        computer[i].push_input(input_vector[i])

    input_value = 0
    for i in range(0, 5):
        try:
            computer[i].push_input(input_value)
        except ProcessorEndOfProgramException:
            pass
        input_value = computer[i].read_output()


    output = int(computer[4].read_output())
    print(input_vector, output)
    if max_output < output:
        max_output = output
        max_vector = input_vector

print("MAX:", max_vector, max_output)
