# Time to make this program to operate more like processor

def get_addresses(modes):
    addresses = []
    i = 1
    for item in (reversed(modes)):
        if item == "0":  # position (addressed) mode
            addresses.append(int(p_mem[pc + i]))
        if item == "1":  # immediate (direct address) mode
            addresses.append(pc + i)
        i += 1
    return addresses


def addition(addresses):
    p_mem[addresses[2]] = str(int(p_mem[addresses[0]]) + int(p_mem[addresses[1]]))
    return 4


def multiplication(addresses):
    p_mem[addresses[2]] = str(int(p_mem[addresses[0]]) * int(p_mem[addresses[1]]))
    return 4


def store(addresses):
    p_mem[addresses[0]] = str(
        int(input("Enter value (PC={}):".format(pc))))  # p_mem are strings, int() to check for valid value
    return 2


def output(addresses):
    print("PC={}, result ".format(pc), p_mem[addresses[0]])
    return 2


def finalize():
    pass


commands = {1: addition, 2: multiplication, 3: store, 4: output, 99: finalize}

with open('input.txt') as f:
    p_mem = f.readline().strip().split(',')
    pc = 0

    cmd = int(p_mem[pc]) % 100  # just two last digits is an opcode

    while commands[cmd] != finalize:
        modes = p_mem[pc].zfill(5)  # max len of istruction is 5
        modes = modes[0:-2]  # but modes are witout last two digits
        addresses = get_addresses(modes)
        pc += commands[cmd](addresses)
        cmd = int(p_mem[pc]) % 100
