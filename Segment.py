from Line import Line
import matplotlib.pyplot as plt
import math

class Segment(Line):
    def __init__(self, xy1=None, xy2=None, color='black'):
        super().__init__(xy1, xy2, color)

    def draw(self, canvas = plt):
        x = (self.xy1[0], self.xy2[0])
        y = (self.xy1[1], self.xy2[1])

        formula = 'y = {}x + {}'.format(self.m, self.b)

        canvas.plot(x, y, label = formula, color = self.color)

        canvas.title('Graph of ' + formula)
        canvas.legend(loc = 'upper left')

        canvas.show()
    
    def Length(self):

        x_length = self.xy2[0] - self.xy1[0]
        y_length = self.xy2[1] - self.xy1[1]

        return math.sqrt(math.pow(x_length, 2) + math.pow(y_length, 2))

    def is_inline(self, point):
        if type(point) == tuple and len(point) == 2:
            if (point[1] == self.m * point[0] + self.b) and (self.xy1[0] <= point[0] <= self.xy2[0]) and (self.xy1[1] <= point[1] <= self.xy2[1]):
                return True
            else:
                return False

        else:
           raise Exception("Not valid value")

    def get_y(self, x):
        if (self.xy1[0] <= x <= self.xy2[0]):
            return super().get_y(x)
        else:
            return None

    def intersect_point(self, line):
        point = super().intersect_point(line)

        if point != None and (min(self.xy1[0], self.xy2[0]) <= point[0] <= max(self.xy1[0], self.xy2[0])) and (min(self.xy1[1], self.xy2[1]) <= point[1] <= max(self.xy1[1], self.xy2[1])):
            return point


        else:
            return None

        

         

         

            

        


test = Segment((0,0), (1, 5))

test2 = Line(m = 2, b = 3)

print(test.intersect_point(test2))

#y = 5x