from random import choice

class Snake:
    
    def __init__(self, length, pos, direction, board_size):
    
        if length != len(pos):
            raise Exception("Length is not equal to the size of `pos`")
        self.len    = length
        self.pos    = pos
        self.dir    = direction
        self.last   = pos[-1]
        self.first  = pos[0]
        self.columns= board_size[0]
        self.rows   = board_size[1]

    def move_toward_direction(self, step = 1, increment_size=False):

        temp = self.last[:]
        if self.dir.upper() == "UP":
            temp[0] -= 1
            if self.check(temp):
                self.pos.append(temp)
            else:
                self.__lost()

        elif self.dir.upper() == "DOWN":
            temp[0] += 1
            if self.check(temp):
                self.pos.append(temp)
            else:
                self.__lost()

        elif self.dir.upper() == "RIGHT":
            temp[1] += 1
            """
            if temp[1] >= self.columns:
                temp[1] = 0
            elif temp[1] <= 0:
                temp[1] = self.columns-1
            """
            if self.check(temp):
                self.pos.append(temp)
            else:
                self.__lost()

        elif self.dir.upper() == "LEFT":
            temp[1] -= 1
            """
            if temp[1] >= self.columns:
                temp[1] = 0
            elif temp[1] <= 0:
                temp[1] = self.columns-1
            """
            if self.check(temp):
                self.pos.append(temp)
            else:
                self.__lost()

        else:
            raise Exception(f"Direction not correct!: {self.dir}")

        #if (not increment_size) and (self.len>1):
        if not increment_size :
            self.pos.remove(self.first)
            self.first = self.pos[0]
        else:
            self.len += 1
        self.first = self.pos[0]
        self.last  = self.pos[-1]

    
    def check(self, tmp):
        
        if tmp not in self.pos:
            return True
        else:
            return False

    def rand_direction(self):
        
        counter = 0

        while True:
            
            tmp = choice(["UP","RIGHT","LEFT","DOWN"])
            #chcs = [i for i in ["UP","RIGHT","LEFT","DOWN"] if self.check(i)]
            temp = self.last[:]
            if tmp == "UP"     :
                temp[0] -= 1

            elif tmp == "DOWN" :
                temp[0] += 1

            elif tmp == "RIGHT":
                temp[1] += 1

            elif tmp == "LEFT" :
                temp[1] -= 1

            else:
                raise Exception(f"Direction not correct!: {tmp}")
     
            if self.check(temp):
                self.dir = tmp
                return
            counter += 1
            if counter > 32:
                raise Exception("No movement is possible")

    def __lost(self):
        print("__LOST")
        pass            

