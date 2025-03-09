from colorama import Fore, Back, Style, init

# Initialize colorama
init()

# Define colors using colorama
COLOR_BOX = Fore.YELLOW + Back.BLACK
COLOR_BOX_ON_GOAL = Fore.CYAN + Back.BLACK
COLOR_PLAYER = Fore.GREEN + Back.BLACK
COLOR_PLAYER_ON_GOAL = Fore.RED + Back.BLACK
COLOR_WALL = Fore.BLUE + Back.BLACK
COLOR_GOAL = Fore.MAGENTA + Back.BLACK
COLOR_FLOOR = Fore.BLACK + Back.BLACK
COLOR_RESET = Style.RESET_ALL
COLOR_CLEAR_SCREEN = "\033c"  # This is still an ANSI escape code

# Define the symbols that may appear in the board
SYMBOL_BOX = "$"
SYMBOL_BOX_ON_GOAL = "*"
SYMBOL_PLAYER = "@"
SYMBOL_PLAYER_ON_GOAL = "+"
SYMBOL_GOAL = "."
SYMBOL_WALL = "#"
SYMBOL_FLOOR = "-"

# Define the mapping of board symbols to colors
symbolColorMapping = {
    SYMBOL_BOX: COLOR_BOX,
    SYMBOL_BOX_ON_GOAL: COLOR_BOX_ON_GOAL,
    SYMBOL_PLAYER: COLOR_PLAYER,
    SYMBOL_PLAYER_ON_GOAL: COLOR_PLAYER_ON_GOAL,
    SYMBOL_WALL: COLOR_WALL,
    SYMBOL_GOAL: COLOR_GOAL,
    SYMBOL_FLOOR: COLOR_FLOOR,
}

class Model:
    def __init__(self, xsb_file):
        self.board = self.read_file(xsb_file)

    def read_file(self, xsb_file):
        '''read `xsb_file` and return a two-dimensional array.'''
        with open(xsb_file, "r") as f:
            return [list(line.strip()) for line in f]

    def get_player_position(self):
        '''scan board for the player's position. Returns a tuple.'''
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell in {SYMBOL_PLAYER, SYMBOL_PLAYER_ON_GOAL}:
                    return (x, y)

    def is_empty(self, x, y):
        '''checks if the given x, y position is empty (valid for the player or a box to move into)'''
        return self.board[y][x] in {SYMBOL_FLOOR, SYMBOL_GOAL}

    def is_box(self, x, y):
        '''checks if the given x, y position is a box.'''
        return self.board[y][x] in {SYMBOL_BOX, SYMBOL_BOX_ON_GOAL}

    def move(self, dx, dy):
        (x, y) = self.get_player_position()
        (nx, ny) = (x + dx, y + dy)  # nx, ny are where the player is trying to go

        if self.is_empty(nx, ny):
            if self.board[ny][nx] == SYMBOL_GOAL:
                self.board[ny][nx] = SYMBOL_PLAYER_ON_GOAL
            else:
                self.board[ny][nx] = SYMBOL_PLAYER

            if self.board[y][x] == SYMBOL_PLAYER_ON_GOAL:
                self.board[y][x] = SYMBOL_GOAL
            else:
                self.board[y][x] = SYMBOL_FLOOR

        elif self.is_box(nx, ny):
            (nnx, nny) = (nx + dx, ny + dy)  # nnx, nny are where the box is trying to go
            if self.is_empty(nnx, nny):
                if self.board[nny][nnx] == SYMBOL_GOAL:
                    self.board[nny][nnx] = SYMBOL_BOX_ON_GOAL
                else:
                    self.board[nny][nnx] = SYMBOL_BOX

                if self.board[ny][nx] == SYMBOL_BOX_ON_GOAL:
                    self.board[ny][nx] = SYMBOL_PLAYER_ON_GOAL
                else:
                    self.board[ny][nx] = SYMBOL_PLAYER

                if self.board[y][x] == SYMBOL_PLAYER_ON_GOAL:
                    self.board[y][x] = SYMBOL_GOAL
                else:
                    self.board[y][x] = SYMBOL_FLOOR
            else:
                return "can't push this box"
        else:
            return "can't push walls"

class View:
    def __init__(self):
        init()  # Initialize colorama

    def print_board(self, board):
        '''print the board.'''
        print(COLOR_CLEAR_SCREEN)  # clear screen
        for row in board:
            colored_row = "".join(symbolColorMapping[cell] + cell for cell in row)
            print(colored_row + COLOR_RESET)  # Reset color at the end of each line

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_input(self, player_movement):
        match player_movement:
            case 'w':
                invalid = self.model.move(0, -1)
            case 'a':
                invalid = self.model.move(-1, 0)
            case 's':
                invalid = self.model.move(0, 1)
            case 'd':
                invalid = self.model.move(1, 0)
            case 'r':
                self.model.board = self.model.read_file("SOKOBAN_PROJECT/level1.xsb.txt")
                invalid = None
            case 'q':
                return False
            case _:
                print("invalid command")
                invalid = True
        if not invalid:
            self.view.print_board(self.model.board)
        return True

if __name__ == "__main__":
    model = Model("SOKOBAN_PROJECT/level1.xsb.txt")
    view = View()
    controller = Controller(model, view)

    view.print_board(model.board)
    while True:
        player_movement = input("enter move (w, a, s, d), restart (r), or quit (q):")
        if not controller.handle_input(player_movement):
            break