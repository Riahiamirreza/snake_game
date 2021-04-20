from random import randint

class Board:
        
        def __init__(self, columns, rows, fill):
            self.board = [[0 for j in range(columns)] for i in range(rows)]
            self.fill  = fill
            self.col   = columns
            self.rows  = rows
            self.first = fill[-1]
            self.put_food(fill)
  
   

        def board_init(self, fill):

            self.board = [[0 for j in range(self.col)] for i in range(self.rows)]
            self.fill  = fill
            self.first = fill[-1]
            
            for i in self.fill:
                if i == self.first:
                    self.board[i[0]%self.rows][i[1]%self.col] = 2
                else:
                    self.board[i[0]%self.rows][i[1]%self.col] = 1

            self.board[self.food[0]][self.food[1]] = 3
        
        
        def food_process(self, fill):
    
            if self.check_food(fill):
                self.put_food(fill)
            

        def check_food(self, fill):
        
            if self.food in fill:
                return True

            return False

 
        def put_food(self, fill):
            
            while True:
                x,y = randint(0,self.col-1), randint(0, self.rows-1)            
                if [x,y] not in fill:
                    self.board[x][y] = 3
                    self.food        = [x,y]
                    return
            

        
        def show_board(self, snake):
            
            board_ = ""
            for i in self.board:
                for j in i:
                    if j==1:
                        board_ += "@|"
                    elif j==2:

                        if snake.dir == "UP":
                            board_ += "^|"
                        elif snake.dir == "LEFT":
                            board_ += "<|"
                        elif snake.dir == "RIGHT":
                            board_ += ">|"
                        elif snake.dir == "DOWN":
                            board_ += "˅|"

                    elif j==3:
                        board_ += "*|"
                    else:
                        board_ += " |"

                board_ += "\n"
                board_ += "".join(["_ "*self.col])
                board_ += "\n"
                
            print(board_)
