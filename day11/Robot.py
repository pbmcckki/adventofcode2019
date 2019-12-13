from collections import deque


class Robot:
    black = 0
    white = 1
    left = 0
    right = 1

    def __init__(self):
        self.painting = dict()
        self.x, self.y = 0, 0
        self.changes = 0
        self.moves = 0
        self.directions = deque([(0, -1), (-1, 0), (0, 1), (1, 0)])

    def get_color(self):
        return self.painting.get((self.x, self.y), Robot.black)

    def move(self, turn):
        self.moves += 1
        if turn == self.left:
            self.directions.rotate(-1)
        else:
            self.directions.rotate(1)
        self.x += self.directions[0][0]
        self.y += self.directions[0][1]

    def paint(self, color):
        if (self.x, self.y) not in self.painting.keys() and color == self.white:
            self.changes += 1
        self.painting[(self.x, self.y)] = color

    def get_changes(self):
        return self.changes

    def get_text_picture(self):
        min_x = min((x[0] for x in self.painting.keys()))
        min_y = min((x[1] for x in self.painting.keys()))
        max_x = max((x[0] for x in self.painting.keys()))
        max_y = max((x[1] for x in self.painting.keys()))

        picture = [ [" " for x in range(0,max_x-min_x+1)] for y in range(0,max_y-min_y+1)]
        for coords, color in self.painting.items():

            if color == Robot.white:
                picture[coords[1]][coords[0]] = "#"

        return picture
