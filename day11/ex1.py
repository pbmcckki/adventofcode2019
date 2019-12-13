import Processor
import Robot

with open('input.txt') as f:
    common_code = f.readline().strip().split(',')

computer = Processor.Processor(common_code, 0)
painter = Robot.Robot()

computer.reset()
try:
    while True:
        try:
            computer.run()
            computer.push_input(painter.get_color())
        except Processor.ProcessorOutputException:
            color, direction = computer.read_output()
            painter.paint(color)
            painter.move(direction)
except Processor.ProcessorEndOfProgramException:
    print(painter.get_changes())

