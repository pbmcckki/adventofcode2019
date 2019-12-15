import Processor

with open('input.txt') as f:
    common_code = f.readline().strip().split(',')


computer = Processor.Processor(common_code, 0)

computer.reset()
blocks = set()
try:
    while True:
        try:
            computer.run()
        except Processor.ProcessorOutputException:
            x, y, t = computer.read_output()
            if t == 2:
                blocks.add((x, y))

except Processor.ProcessorEndOfProgramException:
    print(len(blocks))
