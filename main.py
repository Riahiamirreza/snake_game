from time   import sleep
from random import choice
from snake  import Snake
from board  import Board

pos = [
    [1,1], [1,2], [2,2],
    [2,3], [2,4], [2,5], 
    [3,5], [4,5], [4,6], 
    [5,6], [6,6], [7,6],
    [8,6], [8,7], [8,8],
    [9,8], [10,8], [11,8]
]


s = Snake(len(pos), pos, "UP",[10,10])
b = Board(15,15,s.pos)
print('\033c')

for i in range(100):
    
    s.rand_direction()
    s.move_toward_direction()
    b.food_process(s.pos)
    b.board_init(s.pos)
    b.show_board(s)
    sleep(.3)
    print('\033c')




