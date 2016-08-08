import numpy
import math

size_of_grid = 50
pi = math.pi

torus_points = numpy.zeros((size_of_grid ** 2, 4))
counter_of_points = 0

for step1 in range(0, size_of_grid):
    for step2 in range(0, size_of_grid):

        angle1 = step1 * 2 * pi / size_of_grid
        angle2 = step2 * 2 * pi / size_of_grid
        torus_points[counter_of_points, 0] = math.cos(angle1)
        torus_points[counter_of_points, 1] = math.sin(angle1)
        torus_points[counter_of_points, 2] = math.cos(angle2)
        torus_points[counter_of_points, 3] = math.sin(angle2)

        counter_of_points = counter_of_points + 1

from sklearn.manifold import TSNE

tsne_object = TSNE(n_components=3, method="exact")
embedding = tsne_object.fit_transform(torus_points)

import pylab
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

fig = pylab.figure()
ax = Axes3D(fig)

ax.plot_wireframe(embedding[:,0], embedding[:,1], embedding[:,2])
pyplot.show()
