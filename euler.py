import matplotlib.pyplot as plot
import numpy as np
import scipy.integrate as integrate

class Euler:
    def __init__(self):
        self.figure = plot.figure()
        self.axes = self.figure.gca()

        # k(t) is some continuous/differentiable function.
        # Different curves result in different shape of euler spiral
        # When k=0, the parametric representation yields the x-axis
        # When k=1, it yields the circle (1 = x**2 + (y - 1)**2)
        self.f = lambda t: t**2

    def x(self, t, step=0.001):
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

def test():
    import numpy as np
    from scipy.special import fresnel
    import pylab
    t = np.linspace(-10, 10, 100)
    pylab.plot(*fresnel(t), c='k')
    pylab.show()

def main():
    print("Starting...")
    # Global settings
    plot.rcParams['legend.fontsize'] = 10

    euler = Euler()
    euler.draw()
    #test()
    print("Done")

if __name__ == '__main__':
    exit(main())