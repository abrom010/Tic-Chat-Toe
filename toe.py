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

    rows = {"toprow":[upleft,upmid,upright], "midrow":[midleft,center,midright], "botrow":[botleft,botmid,botright]}
    columns = {"leftcol":[upleft,midleft,botleft], "midcol":[upmid,center,botmid], "rightcol":[upright,midright,botright]}
    diagonals = {"decrease":[upleft,center,botright], "increase":[upright,center,botleft]}

    groups = [rows,columns,diagonals]

    #checks for game_over
    def check(self):
        for group in self.groups:
            for boxes in group.values():
                winners = boxes
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
                            
                            
                            for item in group:
                                if group[item] == winners:
                                    return item
                            

if __name__ == "__main__":
    board = Board()
    #for box in board.rows["toprow"]:
     #   box.fill()
    
    print(board.check())
    print(board.game_over)
 