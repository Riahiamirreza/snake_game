from time import sleep
from snake import Snake
from board import Board


class Game:
    
    def __init__(self):
        pass

    def new_game(self, board_dim = [10, 10], level = "EASY"):

        #self.snake = Snake(1, [[int(board_dim[0]/2), int(board_dim[1]/2)]], "UP", board_dim)
        self.snake = Snake(2, [[2,2],[2,3]], "UP", board_dim)
        self.board = Board(board_dim[0], board_dim[1], self.snake.pos)

    def run(self):

        self.score = 0
        while True:
            print('\033c')
            self.snake.rand_direction()
            self.board.food_process(self.snake.pos)
            #if self.board.check_food(self.snake.pos):
            if self.board.eaten:
                self.score += 1
                self.snake.move_toward_direction(increment_size=True)
            else:
                self.snake.move_toward_direction()
            self.board.board_init(self.snake.pos)
            self.board.show_board(self.snake)
            print(self.snake.pos, self.board.food, f" score:{self.score}")
            sleep(.2)
            
                
