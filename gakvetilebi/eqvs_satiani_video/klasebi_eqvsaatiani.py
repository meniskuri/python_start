# rogorc chans classebit obieqtebit da konstruqtorebit
# momiwevs pythonzec snake is dawerac. grr... fuck

class Point:
    # konstruqtori
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        print("move")
        self.x = self.x + 1

    def draw(self):
        print("draw")

sheviyvanot_x = 4

point1 = Point(sheviyvanot_x,3)
point1.move()
#point1.x = 1
print(point1.x)
