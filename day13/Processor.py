# Time to make this to more OOP as it gets fairly complex by now
from Memory import Memory


class ProcessorInputException(Exception):
    def __init__(self, id):
        self.id = id


class ProcessorOutputException(Exception):
    def __init__(self, id):
        self.id = id


class ProcessorEndOfProgramException(Exception):
    def __init__(self, id):
        self.id = id


class Processor:
    def __init__(self, screen, program=None, id=0):

        self.commands = {1: self.addition, 2: self.multiplication, 3: self.wait_for_input, 4: self.output,
                         5: self.jump_if_true, 6: self.jump_if_false, 7: self.less_than, 8: self.equals,
                         9: self.adjust_base, 99: self.finalize}
        self.screen = screen
        self.id = id
        self.pc = 0
        self.p_mem = Memory()
        self.input_address = None
        self.output_value = [None, None, None]
        self.output_in_progress = 0
        self.relative_base = 0
        if program:
            self.store_mem = Memory(program)
            self.reset()

    def read_output(self):
        return self.output_value

    def reset(self):
        self.p_mem = Memory()
        self.p_mem = self.store_mem.copy()
        self.pc = 0
        self.relative_base = 0
        self.input_address = None
        self.output_value = [None, None, None]
        self.output_in_progress = 0

    def run(self):
        cmd = int(self.p_mem[self.pc]) % 100  # just two last digits is an opcode
        while True:
                modes = self.p_mem[self.pc].zfill(5)  # max len of instruction is 5
                modes = modes[0:-2]  # but modes are without last two digits
                addresses = self.get_addresses(modes)
                command = self.commands[cmd]
                step = command(addresses)
                self.pc += step
                cmd = int(self.p_mem[self.pc]) % 100

    def get_addresses(self, modes):
        addresses = []
        i = 1
        for item in (reversed(modes)):
            if item == "0":  # position (addressed) mode
                if (self.pc + i) >= len(self.p_mem):
                    break
                addresses.append(int(self.p_mem[self.pc + i]))
            if item == "1":  # immediate (direct address) mode
                addresses.append(self.pc + i)
            if item == "2":  # relative addressing mode
                if (self.pc + i) >= len(self.p_mem):
                    break
                addresses.append(self.relative_base + int(self.p_mem[self.pc + i]))
            i += 1
        return addresses

    def addition(self, addresses):
        self.p_mem[addresses[2]] = str(int(self.p_mem[addresses[0]]) + int(self.p_mem[addresses[1]]))
        return 4

    def multiplication(self, addresses):
        self.p_mem[addresses[2]] = str(int(self.p_mem[addresses[0]]) * int(self.p_mem[addresses[1]]))
        return 4

    def wait_for_input(self, addresses):
        self.input_address = addresses[0]
        raise ProcessorInputException(self.id)

    def push_input(self, data):
        self.p_mem[self.input_address] = str(data)
        self.input_address = None
        self.pc += 2
        # self.run()

    def output(self, addresses):

        self.output_value[self.output_in_progress] = int(self.p_mem[addresses[0]])
        if self.output_in_progress == 2:
            self.output_in_progress = 0
            self.pc += 2
            raise ProcessorOutputException(self.id)
        else:
            self.output_in_progress += 1
            return 2

    def jump_if_true(self, addresses):
        if int(self.p_mem[addresses[0]]) != 0:
            self.pc = int(self.p_mem[addresses[1]])
            return 0
        return 3

    def jump_if_false(self, addresses):
        if int(self.p_mem[addresses[0]]) == 0:
            self.pc = int(self.p_mem[addresses[1]])
            return 0
        return 3

    def less_than(self, addresses):
        if int(self.p_mem[addresses[0]]) < int(self.p_mem[addresses[1]]):
            self.p_mem[addresses[2]] = "1"
        else:
            self.p_mem[addresses[2]] = "0"
        return 4

    def equals(self, addresses):
        if int(self.p_mem[addresses[0]]) == int(self.p_mem[addresses[1]]):
            self.p_mem[addresses[2]] = "1"
        else:
            self.p_mem[addresses[2]] = "0"
        return 4

    def adjust_base(self, addresses):
        self.relative_base += int(self.p_mem[addresses[0]])
        return 2

    def finalize(self, addresses):
        raise ProcessorEndOfProgramException(self.id)
