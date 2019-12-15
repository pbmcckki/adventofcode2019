import Processor
import Board
import curses
import time
from curses import wrapper

new_screen = curses.initscr()

key_map = {-1: '0', curses.KEY_LEFT: '-1', curses.KEY_RIGHT: '1'}


def main(new_screen):
    new_screen.timeout(500)  # Slow speed
    with open('input.txt') as f:
        common_code = f.readline().strip().split(',')

    computer = Processor.Processor(new_screen,common_code, 0)

    computer.reset()
    blocks = dict()

    # Load blocks first
    try:
        while True:
            try:
                computer.run()
            except Processor.ProcessorOutputException:
                x, y, t = computer.read_output()
                blocks[(x, y)] = t

    except Processor.ProcessorEndOfProgramException:
        board = Board.Board(blocks, new_screen)
        print(len(blocks))

    # Lets play
    common_code[0] = '2'
    computer = Processor.Processor(new_screen,common_code, 0)

    computer.reset()
    try:
        while True:
            try:
                new_screen.addstr(3, 1, "RUNNING {0} {1:5s}".format(computer.pc, computer.p_mem[computer.pc]))
                new_screen.refresh()
                computer.run()
            except Processor.ProcessorOutputException:
                new_screen.addstr(3, 1, "OUTPUT")
                new_screen.refresh()
                x, y, t = computer.read_output()
                new_screen.addstr(1, 1, "{}  {}  {}".format(x, y, t))
                new_screen.refresh()
                if x == -1 and y == 0:
                    board.update_score(t)
                else:
                    board.update_point(x, y, t)
            except Processor.ProcessorInputException:
                new_screen.addstr(3, 1, "INPUT")
                new_screen.refresh()

                board.refresh()

                c = key_map.get(new_screen.getch(),'0')
                computer.push_input(c)

    except Processor.ProcessorEndOfProgramException:
        new_screen.addstr(0, 0, "Game Over")
        new_screen.timeout(-1)
        new_screen.getch()


wrapper(main)
