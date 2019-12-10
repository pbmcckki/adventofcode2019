from Processor import Processor, ProcessorEndOfProgramException

with open('input_d9.txt') as f:
    common_code = f.readline().strip().split(',')
# common_code = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
# common_code = [str(x) for x in common_code]

computer = Processor(common_code, 0)

computer.reset()
try:
    computer.run()
    computer.push_input(1)
except ProcessorEndOfProgramException:
    print(computer.read_output())
