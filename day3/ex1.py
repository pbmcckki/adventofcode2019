board = dict()
sumlen = 0
with open('input.txt') as f:
    commands = f.readline().strip().split(',')
    c_x, c_y = 0, 0
    for command in commands:
        direction = command[0]
        length = int(command[1:])
        if direction == "L":
            for x in range(c_x - length, c_x):
                board[(x, c_y)] = 1
            c_x = c_x - length
        if direction == "R":
            for x in range(c_x + 1, c_x + length + 1):
                board[(x, c_y)] = 1
            c_x = c_x + length
        if direction == "D":
            for y in range(c_y - length, c_y):
                board[(c_x, y)] = 1
            c_y = c_y - length
        if direction == "U":
            for y in range(c_y + 1, c_y + length + 1):
                board[(c_x, y)] = 1
            c_y = c_y + length



    commands = f.readline().strip().split(',')
    c_x, c_y = 0, 0
    for command in commands:
        direction = command[0]
        length = int(command[1:])
        if direction == "L":
            for x in range(c_x - length, c_x):
                if board.get((x, c_y), 2) != 2:
                    board[(x, c_y)] = 'X'
                else:
                    board[(x, c_y)] = 2
            c_x = c_x - length
        if direction == "R":
            for x in range(c_x + 1, c_x + length + 1):
                if board.get((x, c_y), 2) != 2:
                    board[(x, c_y)] = 'X'
                else:
                    board[(x, c_y)] = 2
            c_x = c_x + length
        if direction == "D":
            for y in range(c_y - length, c_y):
                if board.get((c_x, y), 2) != 2:
                    board[(c_x, y)] = 'X'
                else:
                    board[(c_x, y)] = 2
            c_y = c_y - length
        if direction == "U":
            for y in range(c_y + 1, c_y + length + 1):
                if board.get((c_x, y),2) != 2:
                    board[(c_x, y)] = 'X'
                else:
                    board[(c_x, y)] = 2
            c_y = c_y + length

    crossings = [abs(k[0]) + abs(k[1]) for k in board if board[k] == "X"]
    print(min(crossings))
