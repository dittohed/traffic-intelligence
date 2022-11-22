from pyswarms.single.global_best import GlobalBestPSO
from pyswarms.utils.plotters import plot_contour
from pyswarms.utils.plotters.formatters import Mesher, Designer


def rosenbrock(xs, a, b):
    fs = (a - xs[:, 0]) ** 2 + b * (xs[:, 1] - xs[:, 0] ** 2)  ** 2
    return fs


if __name__ == '__main__':
    options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
    optimizer = GlobalBestPSO(n_particles=10, dimensions=2, options=options)

    cost, pos = optimizer.optimize(rosenbrock, iters=1000, a=1, b=100)

    animation = plot_contour(pos_history=optimizer.pos_history,
                             mesher=Mesher(func=lambda xs: rosenbrock(xs, 1, 100)),
                             designer=Designer(limits=[(-1, 2), (-1, 2)], label=['x-axis', 'y-axis']),
                             mark=(1,1))
    animation.save('rosenbrock.gif', fps=10)