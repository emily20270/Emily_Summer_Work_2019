import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

class Bateman(object):

    def __init__(self, t, N, n, L, l):
        self.t = t
        self.N = N
        self.n = n
        self.L = L
        self.l = l
        self.Activity1 = []
        self.Activity2 = []

    def Activity(self):
        lg = np.log(2)
        print(lg)
        lam1 = lg/float(self.L)
        lam2 = lg/float(self.l)
        T = np.linspace(0,float(t),100)
        Activity1 = []
        Activity2 = []
        for i in T:
            Act1 = lam1*self.N*np.exp(-lam1*i)
            self.Activity1.append(Act1)
            Act2sect1 = (lam1*lam2)/(lam2-lam1)
            Act2sect2 = self.N*(np.exp(-lam1*i)-np.exp(-lam2*i))
            Act2sect3 = lam2*self.n*np.exp(-lam2*i)
            Act2 = Act2sect1*Act2sect2+Act2sect3
            self.Activity2.append(Act2)
            print(Act2sect3)
        print(self.Activity1[-1])
        print(self.Activity2[-1])

    def Plot(self):
        print(self.Activity1)
        T = np.linspace(0,float(t),100)
        plt.plot(T, self.Activity1)
        plt.plot(T, self.Activity2)
        plt.title("Radioisotope Activity")
        plt.xlabel("time (min.)")
        plt.ylabel("becquerels (Bq)")
        plt.legend(("Activity 1", "Activity 2"), loc = "best")
        plt.show()

if __name__ =="__main__":
    t = input("Amount of time passed (in minutes): ")
    Mol = input("Initial amount of original substance (in moles): ")
    Min = input("Half life of substance one (in minutes): ")
    mole = input("Initial amount of secondary substance (in moles): ")
    min = input("Half life of secondary substance (in minutes): ")
    #active = input("Activity of primary substance (in becquerels): ")
    #active2 = input("Activity of secondary substance (in becquerels): ")
    t = float(t)
    N = float(6.022140857e+23*float(Mol))
    L = 60*float(Min)
    n = float(6.022140857e+23*float(mole))
    l = 60*float(min)
    equate = Bateman(t,N,n,L,l)
    #if Activity = "?"
    nexted = equate.Activity()
    ended = equate.Plot()
