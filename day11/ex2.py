import Processor
import Robot
import Robot

with open('input.txt') as f:
    common_code = f.readline().strip().split(',')

computer = Processor.Processor(common_code, 0)
painter = Robot.Robot()
painter.paint(Robot.Robot.white)

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
    picture = painter.get_text_picture()

for line in picture:
    for x in line:
        print(x, end="")
    print()
