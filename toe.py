''' CLASS '''
class Box:
    isFilled = False
    hasCircle = False
    isDiagonal = False

    def __init__(self, isDiagonal=False):
        self.isDiagonal = isDiagonal

    #call with an argument to fill box with o, otherwise with x
    def fill(self,hasCircle=False):
        self.isFilled = True

        if hasCircle:
            self.hasCircle = True
        else:
            pass

''' CLASS '''

class Board:
    square_won = False
    circle_won = False
    game_over = False

    upleft,upmid,upright,midleft,center,midright,botleft,botmid,botright = \
    Box(True),Box(),Box(True),Box(),Box(True),Box(),Box(True),Box(),Box(True)

    boxes = {"upleft":upleft,"upmid":upmid,"upright":upright,"midleft":midleft,"center":center,"midright":midright,"botleft":botleft,"botmid":botmid,"botright":botright}
    rows = [[upleft,upmid,upright],[midleft,center,midright],[botleft,botmid,botright]]
    columns = [[upleft,midleft,botleft],[upmid,center,botmid],[upright,midright,botright]]

    ''' BIG FUNCTION '''

    #checks for game_over
    def check(self):
        center = self.boxes["center"]

        if center.isFilled:
            searchList = {}
            for (name,box) in self.boxes.items():
                if box == center or not box.isDiagonal:
                    pass
                else:
                    if box.isFilled and box.hasCircle == center.hasCircle:
                        searchList.update({name:box})
            
            if len(searchList) > 1:
                for name in searchList.keys():
                    win_string = ""
                    if "up" in name:
                        win_string+= "bot"
                    else:
                        win_string+= "up"

                    if "left" in name:
                        win_string+= "right"
                    else:
                        win_string+= "left"

                    for name in searchList.keys():
                        if name == win_string:
                            if center.hasCircle == True:
                                self.circle_won = True
                            else:
                                self.square_won = True
                        self.game_over = True
        print(self.game_over)

        for row in self.rows:
            ctr = 0
            first = row[0]

            if first.isFilled:
                for box in row:
                    if box == first:
                        pass
                    else:
                        if box.isFilled == first.isFilled and box.hasCircle == first.hasCircle:
                            ctr+=1
                    if ctr > 1:
                        if first.hasCircle == True:
                            self.circle_won = True
                        else:
                            self.square_won = True
                        self.game_over = True
                        break

        for column in self.columns:
            ctr = 0
            first = column[0]

            if first.isFilled:
                for box in column:
                    if box == first:
                        pass
                    else:
                        if box.isFilled == first.isFilled and box.hasCircle == first.hasCircle:
                            ctr+=1
                    if ctr > 1:
                        if first.hasCircle == True:
                            self.circle_won = True
                        else:
                            self.square_won = True
                        self.game_over = True
                        break
        print(self.game_over)

        ''' BIG FUNCTION '''

''' CLASS '''

if __name__ == "__main__":
    board = Board()
    board.check()