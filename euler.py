import matplotlib.pyplot as plot
import numpy as np
from scipy.special import fresnel
import scipy.integrate as integrate

class Euler:
    def __init__(self):
        self.figure = plot.figure()
        self.axes = self.figure.gca()

        # f(t) is some continuous/differentiable function.
        # Different curves result in different shape of euler spiral
        # You must manually solve for these yourself
        self.f = lambda t: t*np.cos(t)
        self.f_prime = lambda t: np.cos(t) - t * np.sin(t)

    def k(self, t):
        '''
        curvature
        '''
        return self.f_prime(t)


    def x(self, t, step=0.01):
        '''
        x(t) = integral( cos(f(t) dt )
        Integral is approximated with rectangles
        '''
        aggregate = 0
        t_range = np.arange(0, t, step).tolist()
        for t in t_range:
            aggregate += np.cos(self.f(t)) * step

        return aggregate

    def y(self, t, step=0.01):
        '''
        y(t) = integral( cos(f(t) )
        '''
        aggregate = 0
        t_range = np.arange(0, t, step).tolist()
        for t in t_range:
            aggregate += np.sin(self.f(t)) * step

        return aggregate

    def draw(self, lower_bound=-10, upper_bound=10, step=0.01):
        t_range = np.arange(lower_bound, upper_bound, step).tolist()

        for t in t_range:
            self.axes.plot(self.x(t), self.y(t), markersize=1, marker='o')

        plot.show()

    def drawNegative(self, lower_bound=-10, upper_bound=10, step=0.01):
        t_range = np.arange(lower_bound, upper_bound, step).tolist()

        for t in t_range:
            self.axes.plot(-self.x(t), -self.y(t), markersize=1, marker='o')

        plot.show()


    def drawFresnel(self, lower_bound=-100, upper_bound=100, step=0.01):
        t_range = np.arange(lower_bound, upper_bound, step)
        for t in t_range:
            (S, C) = fresnel(t)
            self.axes.plot(S, C, markersize=1, marker='x')

        plot.show()

def main():
    print("Starting...")
    # Global settings
    plot.rcParams['legend.fontsize'] = 10

    euler = Euler()
    euler.draw()
    #euler.drawNegative()
    #euler.drawFresnel()

    print("Done")

if __name__ == '__main__':
    exit(main())