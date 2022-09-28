import imp
import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib.colors as mcolors
import abc



class Line:
    def __init__(self, xy1 = None, xy2 = None, m = None, b = None, color = 'black'):
        if m != None and b != None:
            if type(m) == int or type(m) == float:
                if type(b) == int or type(b) == float:
                    self.b = b
                    self.m = m
                    self.color = color

                else:
                    raise Exception("b must be int or float")
            else:
                raise Exception("m must be int or float")
                

            
        elif xy1 != None and xy2 != None:
            if (type(xy1) == tuple and type(xy2) == tuple) and (len(xy1) == 2 and len(xy2) == 2):
                self.xy1 = xy1
                self.xy2 = xy2

                self.m = (self.xy1[1] - self.xy2[1]) / (self.xy1[0] - self.xy2[0])
                self.b = self.xy1[1] - (self.xy1[0] * self.m)
                self.color = color

            else:
                raise Exception("You must enter a tupple for x and y")



        elif (xy1 != None or xy2!= None) and m != None:

            if xy1 != None and type(xy1) == tuple and len(xy1) == 2:
                self.m = m
                self.color = color
                self.b = xy1[1] - (self.m * xy1[0])

            elif xy2 != None and type(xy2) == tuple and len(xy2) == 2:
                self.m = m
                self.color = color
                self.b = xy2[1] - (self.m * xy2[0])
            
            else:
                raise Exception("You must enter a tupple for x and y")

        
        else:
            raise Exception("You cant leave it empty")

    def draw(self, canvas = plt):
        x = np.linspace(-5,5,100)
        y = self.m * x + self.b
        formula = 'y = {}x + {}'.format(self.m, self.b)

        canvas.plot(x, y, label = formula, color = self.color)

        canvas.title('Graph of ' + formula)
        canvas.legend(loc = 'upper left')

        canvas.show()


    def __str__(self):
        formula = 'y = {}x + {}'.format(self.m, self.b)

        return f'The formula is ' + formula

    def Equation(self):
        self.Line(self.xy1, self.xy2)

    def get_equation(self):
        return self.__str__()

    def set_color(self, color):
        supported_colors = list(mcolors.CSS4_COLORS.keys())

        if supported_colors.__contains__(color):
            self.color = color

        else:
            raise Exception("Not valid value")

    def is_inline(self, point):
        if type(point) == tuple and len(point) == 2:
            if point[1] == self.m * point[0] + self.b:
                return True
            else:
                return False

        else:
           raise Exception("Not valid value")

    def is_perpendicular(self, formula):
        if type(formula) == Line:
            if self.m / formula.m == -1:
                return True

            else:
                return False
        else:
            raise Exception("Not valid value")

    def get_perpendicular(self, point):
        if type(point) == tuple and len(point) == 2:
            if point[1] == self.m * point[0] + self.b:
                return Line(point, m = -1 / self.m)

            else:
                raise Exception("the point isn't on the Line")
        else:
            raise Exception("Not valid value")
        
    def get_y(self, x):
        if type(x) == int or type(x) == float:
            return self.m * x + self.b
        else:
            raise Exception("x needs to be int or float")

    def intersect_point(self, line):
        if self.m == line.m:
            return None

        else:
            x = self.m - line.m 
            b = line.b - self.b

            temp = x #divide by a num

            x = x / temp
            b = b / temp 

            if x < 0:
                x *= -1
                b *= -1

            
            return (b, self.get_y(b))
    
    def is_intersect(self, line):
       if self.intersect_point(line) is None:
        return False

       return True 