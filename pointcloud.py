import random
import numpy as np
from matplotlib import pyplot

random.seed(10)

def generatePointCloud(n):
    return np.random.randint(-100,100,size=(100,n))

def plot(points):
    xs, ys = map(list, zip(*points))
    pyplot.axis([min(xs)-1,max(xs)+1,min(ys)-1,max(ys)+1])
    pyplot.plot(xs, ys, 'ro')
    pyplot.show()


#print(generatePointCloud(3))
#plot(generatePointCloud(100))