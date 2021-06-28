from time import sleep
from threading import Thread
from snake import Snake
from board import Board


class Game:
    
    def __init__(self):
        pass

    def new_game(self, board_dim = [10, 10], level = "EASY"):

        self.snake = Snake(2, [[2,2],[2,3]], "UP", board_dim)
        self.board = Board(board_dim[0], board_dim[1], self.snake.pos)
        self.thrd  = Thread(target=self.snake.check_arrow_keys)
        self.score = 0

    def finish_game(self):
        print(f"Your score is {self.score}")
        self.thrd.join()
        exit()
        
    def run(self):

        self.thrd.start()
        while True:

            print('\033c')
            if not self.snake.status:
                break

            self.board.food_process(self.snake.normalize_pos())
            if self.board.eaten:
                self.score += 1
                self.snake.move_toward_direction(increment_size=True)
            else:
                self.snake.move_toward_direction()

            self.board.board_init(self.snake.normalize_pos())
            self.board.show_board(self.snake)
            print(f"score:{self.score}")
            sleep(.2)

        self.finish_game()
            
                
