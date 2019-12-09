from Processor import Processor, ProcessorEndOfProgramException
from itertools import permutations

with open('input.txt') as f:
    common_code = f.readline().strip().split(',')
# common_code = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
# -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
# 53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
# common_code = [str(x) for x in common_code]

computer = [Processor(common_code, i) for i in range(0, 5)]

max_vector = None
max_output = 0

for input_vector in permutations(range(5, 10)):
    # initialize
    for i in range(0, 5):
        computer[i].reset()
        computer[i].run()
        computer[i].push_input(input_vector[i])

    input_value = 0
    while True:
        try:
            print(input_value)
            for i in range(0, 5):
                try:
                    computer[i].push_input(input_value)
                    input_value = computer[i].read_output()
                except ProcessorEndOfProgramException as e:
                    if e.id == 4:
                        raise
                    else:
                        input_value = computer[i].read_output()

        except ProcessorEndOfProgramException:
            break

    output = int(computer[4].read_output())
    print(input_vector, output)
    if max_output < output:
        max_output = output
        max_vector = input_vector

print("MAX:", max_vector, max_output)
