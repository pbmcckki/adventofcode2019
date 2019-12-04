def draw(board, commands):
    c_x, c_y = 0, 0
    for command in commands:
        direction = command[0]
        length = int(command[1:])
        if direction == "L":
            for x in range(c_x-1, c_x - length-1, -1):
                board.append((x, c_y))
            c_x = c_x - length
        if direction == "R":
            for x in range(c_x + 1, c_x + length + 1):
                board.append((x, c_y))
            c_x = c_x + length
        if direction == "D":
            for y in range(c_y-1, c_y - length-1, -1):
                board.append((c_x, y))
            c_y = c_y - length
        if direction == "U":
            for y in range(c_y + 1, c_y + length + 1):
                board.append((c_x, y))
            c_y = c_y + length


with open('input.txt') as f:
    commands = f.readline().strip().split(',')
    board1 = []
    draw(board1, commands)

    commands = f.readline().strip().split(',')
    board2 = []
    draw(board2, commands)

    crossings = set(board1) & set(board2)

    distance = min((board1.index(k) + board2.index(k) + 2 for k in crossings))

    print(distance)
