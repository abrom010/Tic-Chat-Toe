''' CLASS '''
class Box:
    isFilled = False
    hasCircle = False

    #call to fill box
    def fill(self,hasCircle=False):
        self.isFilled = True

        if hasCircle:
            self.hasCircle = True

''' CLASS '''

class Board:
    cross_won = False
    circle_won = False
    game_over = False

    upleft,upmid,upright,midleft,center,midright,botleft,botmid,botright = \
    Box(),Box(),Box(),Box(),Box(),Box(),Box(),Box(),Box()

    boxes = {"upleft":upleft,"upmid":upmid,"upright":upright,"midleft":midleft,"center":center,"midright":midright,"botleft":botleft,"botmid":botmid,"botright":botright}

    rows = [[upleft,upmid,upright],[midleft,center,midright],[botleft,botmid,botright]]
    columns = [[upleft,midleft,botleft],[upmid,center,botmid],[upright,midright,botright]]
    diagonals = [[upleft,center,botright],[upright,center,botleft]]

    groups = [rows,columns,diagonals]

    ''' BIG FUNCTION '''

    #checks for game_over
    def check(self):
        for group in self.groups:
            for boxes in group:
                ctr = 0
                first = boxes[0]

                if first.isFilled:
                    for box in boxes:
                        if box != first and box.isFilled and box.hasCircle == first.hasCircle:
                            ctr+=1

                        if ctr == 2:
                            if first.hasCircle == True:
                                self.circle_won = True
                            else:
                                self.cross_won = True
                            self.game_over = True
                            break

        return(self.game_over)

        ''' BIG FUNCTION '''

''' CLASS '''

if __name__ == "__main__":
    board = Board()
    print(board.check())