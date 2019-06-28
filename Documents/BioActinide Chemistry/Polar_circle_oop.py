import matplotlib.pyplot as plt
import numpy as np

class Circle(object):
    def __init__(self,r):
        self.r = r
        self.theta = []
        self.radius = []

    def  Polar(self):
        N = np.arange(0,360,1)
        for i in N:
            self.theta.append(np.pi*i/180)
            self.radius.append(self.r)

    def Plot(self):
        plt.polar(self.theta, self.radius)
        plt.show()

if __name__ =="__main__":
    plr = Circle(300)
    arange = plr.Polar()
    axis = plr.Plot()
