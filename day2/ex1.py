with open('input.txt') as f:
    p_mem = f.readline().strip().split(',')
    p_mem = [int(i) for i in p_mem]
    p_mem[1] = 12
    p_mem[2] = 2
    pc = 0
    pc_max=len(p_mem)-1
    i, a, b, x = p_mem[pc:4]
    # Note that x may be out of range of initial program but python lists are flexible enough to accommodate
    while i != 99:
        if i == 1:
                p_mem[x] = p_mem[a] + p_mem[b]
        elif i == 2:
            p_mem[x] = p_mem[a] * p_mem[b]
        pc += 4
        i, a, b, x = p_mem[pc:pc+4]
        print(pc)
    print(p_mem[0])
