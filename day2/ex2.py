with open('input.txt') as f:
    p_mem_init = f.readline().strip().split(',')
    p_mem_init = [int(i) for i in p_mem_init]

    for noun in range(0, 100):
        for verb in range(0, 100):
            p_mem = p_mem_init[:]
            pc = 0
            p_mem[1] = noun
            p_mem[2] = verb
            i, a, b, x = p_mem[pc:4]
            # Note that x may be out of range of initial program but python lists are flexible enough to accommodate
            while i != 99:
                if i == 1:
                    p_mem[x] = p_mem[a] + p_mem[b]
                elif i == 2:
                    p_mem[x] = p_mem[a] * p_mem[b]
                else:
                    raise Exception("Something went wrong")
                pc += 4
                i, a, b, x = p_mem[pc:pc + 4]
            if p_mem[0] == 19690720:
                print(100 * noun + verb)
                exit()
