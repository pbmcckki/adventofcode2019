import curses

char_map = {0: ' ', 1: 'W', 2: 'B', 3: '-', 4: 'o'}


class Board:
    def __init__(self, initial_map, screen):
        max_x = max((p[0] for p in initial_map.keys()))
        max_y = max((p[1] for p in initial_map.keys()))

        self.screen = screen
        self.window = curses.newwin(0, 0, max_y, max_x)
        self.score_coords = (max_y + 5, 0)
        self.window.addstr(*self.score_coords, "Score: {0:10d}".format(0))

        # self.blocks = [[0] * (max_x + 1) for i in range(0, max_y + 1)]
        for x, y in initial_map.keys():
            # self.blocks[y][x] = char_map[initial_map.get((x, y), "0")]
            self.window.addch(y, x, char_map[initial_map.get((x, y), 0)])
        self.window.refresh()

    def update_point(self, x, y, c):
        self.window.addch(y, x, char_map[c])

    def refresh(self):
        self.window.refresh()

    def update_score(self, score):
        self.window.addstr(*self.score_coords, "Score: {0:10d}".format(score))
