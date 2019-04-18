import numpy as np
import matplotlib.pyplot as plt


# counts the number of iterations until the function diverges or
# returns the iteration threshold that we check until
def count_iterations_until_divergent(c, threshold):
    z = complex(0, 0)
    for iteration in range(threshold):
        z = (z * z) + c

        if abs(z) > 4:
            break
            pass
        pass
    return iteration


# takes the iteration limit before declaring function as convergent and
# takes the density of the atlas
# create atlas, plot mandelbrot set, display set
def mandelbrot(threshold, density):
    # location and size of the atlas rectangle
    # real_axis = np.linspace(-2.25, 0.75, density)
    # imaginary_axis = np.linspace(-1.5, 1.5, density)
    real_axis = np.linspace(-0.22, -0.219, 1000)
    imaginary_axis = np.linspace(-0.70, -0.699, 1000)
    real_axis_len = len(real_axis)
    imaginay_axis_len = len(imaginary_axis)

    # 2-D array to represent mandelbrot atlas
    atlas = np.empty((real_axis_len, imaginay_axis_len))

    # color each point in the atlas depending on the iteration count
    for ix in range(real_axis_len):
        for iy in range(imaginay_axis_len):
            cx = real_axis[ix]
            cy = imaginary_axis[iy]
            c = complex(cx, cy)

            atlas[ix, iy] = count_iterations_until_divergent(c, threshold)
            pass
        pass

    # plot and display mandelbrot set
    plt.imshow(atlas.T, interpolation="nearest")
    plt.show()


# time to party!!
mandelbrot(120, 1000)
