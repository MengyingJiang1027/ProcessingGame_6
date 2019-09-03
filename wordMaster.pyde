from random import choice

class Brick():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        letters = ["a", "b", "c", "d", "e", "f", "g", 

                   "h", "i", "j", "k", "i", "m", "n", 

                   "o", "p", "q", "r", "s", "t", 

                   "u", "v", "w", "x", "y", "z",

                   "a", "e", "i", "o", "u"]

        self.letter = choice(letters)
        self.picked = False
        self.w = 40
        self.h = 40

    def run(self):
        if self.picked:
            fill(200, 50, 200)
            rect(self.x, self.y, self.w, self.h)
            fill(255)
            text(self.letter, self.x + 15, self.y + 30)
        else:
            fill(255)
            rect(self.x, self.y, self.w, self.h)
            fill(200, 50, 200)
            text(self.letter, self.x + 15, self.y + 30)

    def onclick(self):
        if(self.x < mouseX < self.x + self.w and self.y < mouseY < self.y + self.h):
            if self.picked == False:
                self.picked = True
                return self.letter
            else:
                return ""
        else:
            return ""

class BrickSystem():
    def __init__(self):
        self.trail = ""
        self.row = 8
        self.col = 8
        self.bricks = []
        for row in range(1, self.row + 1):
            rowBrick = []
            for col in range(1, self.col + 1):
                brick = Brick(60 * (col - 1) + 140, 60 * (row - 1) + 130)
                rowBrick.append(brick)
            self.bricks.append(rowBrick)

        
    def run(self):
        for rowBrick in self.bricks:
            for brick in rowBrick:
                brick.run()
    
    def onclick(self):
         for rowBrick in self.bricks:
            for brick in rowBrick:
                letter = brick.onclick()
                if letter == "":
                    self.trail = self.trail
                else:
                    self.trail = self.trail + letter
    
    
    def removeBrick(self):
        for rowBrick in self.bricks:
            for brick in reversed(rowBrick):
                if brick.picked:
                    brick1 = Brick(brick.x, brick.y)
                    rowBrick.remove(brick)
                    rowBrick.append(brick1)
                    
        self.trail = ""
    
    def cleanclick(self):
        self.trail = "" 
        for rowBrick in self.bricks:
            for brick in reversed(rowBrick):
                brick.picked = False

class Game():
    def __init__(self):
        self.currenttrail = ""
        
        self.bricks = BrickSystem()
        
        self.bg = loadImage("bg.jpg")
        
        wordFile = open("words.txt")
        self.wordList = wordFile.readlines()
        for i in range(len(self.wordList)):
            self.wordList[i] = self.wordList[i].rstrip("\n")
        

    def run(self):
    
        self.display()

        self.bricks.run()
    
   
    def onclick(self):
        
        self.bricks.onclick()

        self.check()
        
   
    def cleanclick(self):

        self.currenttrail = ""

        self.bricks.cleanclick()
        

    def display(self):
        image(self.bg, 0, 0, self.bg.width * 0.8, self.bg.height * 0.8)
        fill(0)
        textSize(20)
        text("game target: words contains three or four letters", 140, 650)
        text('''instructions: left click choose letter, 
                    right click cancel choice''', 140, 700)
        text("current letter:", 140, 800)
        text(self.currenttrail, 300, 800)
        

    def check(self):

        self.currenttrail = self.bricks.trail

        for i in range(len(self.wordList)):
 
            if self.wordList[i] == self.currenttrail:
 
                self.bricks.removeBrick()
   
                self.currenttrail = ""
      
                break 
        
        
def setup():
    global game
    game = Game()
    textSize(30)
    size(730, 950)

def draw():
    global game
    game.run()
    

def mousePressed():
    global game

    if mouseButton == LEFT:
        game.onclick()

    elif mouseButton == RIGHT:
        game.cleanclick()
        
        
