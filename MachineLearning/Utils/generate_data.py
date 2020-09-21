import numpy as np

def randomGaussians(numberOfGaussians, stddev, dimension, quantity):

    if numberOfGaussians > 10 or numberOfGaussians <= 0:
        print("Wrong number of center points, try at most 10 and more than 0")
        return

    angleBetweenCenters = 2*np.pi/numberOfGaussians

    print(angleBetweenCenters)

    radiuses = np.random.randint(1,5,(numberOfGaussians))

    for i in range(numberOfGaussians):
        x = np.random.normal(radiuses[i]*np.cos(angleBetweenCenters*i), stddev, quantity)
        y = np.random.normal(radiuses[i]*np.sin(angleBetweenCenters*i), stddev, quantity)
        print(x)
        print(np.array(list(zip(x,y),chr(97+i))))

randomGaussians(3,1,2,5)

