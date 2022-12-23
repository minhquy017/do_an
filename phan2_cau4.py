
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def yen_ngua(z):
    x = np.linspace(-6,6,100)
    y=np.linspace(-6,6,100)

    x, y = np.meshgrid(x, y)
    z = (x / 3) ** 2 - (y / 2) ** 2
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z)
    ax.set_title("đồ thị mặt yên ngựa")
    plt.show()
def hyperbolic_1tang(x,y):
    x, y = np.meshgrid(x, y)
    z1= 2*np.sqrt((x/3)**2+(y/5)**2-1)
    z2= -2*np.sqrt((x/3)**2+(y/5)**2-1)
    fig, ax = plt.subplots(subplot_kw={"projection":
                                           "3d"})
    ax.plot_surface(x, y,z1, cmap="gist_rainbow", linewidth=0, antialiased=False)
    ax.plot_surface(x, y, z2, cmap="gist_rainbow", linewidth=0, antialiased=False)
    ax.set_title("đồ thị hyperbolic 1 tầng")
    plt.show()


def mat_cau(x,y):
    x, y = np.meshgrid(x,y)
    z1 = np.sqrt(4 - (x + 2) ** 2 - (y - 1) ** 2) + 4
    z2= -1*np.sqrt(4 - (x + 2) ** 2 - (y - 1) ** 2) + 4
    fig, ax = plt.subplots(subplot_kw={"projection":
                                           "3d"})
    ax.plot_surface(x, y, z1,cmap="gist_rainbow", linewidth=0, antialiased=False)
    ax.plot_surface(x, y, z2, cmap="gist_rainbow", linewidth=0, antialiased=False)
    ax.set_title("đồ thị mặt cầu")
    plt.show()


def main():
    yen_ngua(2)
    x = np.linspace(start=-10, stop=10,num=5000)
    y = np.linspace(start=-10, stop=10,num=5000)
    b = hyperbolic_1tang(x, y)
    x1 = np.linspace(start=-4, stop=0,num=5000)
    y1 = np.linspace(start=-2, stop=3,num=5000)
    mat_cau(x1,y1)
if __name__=="__main__":
    main()