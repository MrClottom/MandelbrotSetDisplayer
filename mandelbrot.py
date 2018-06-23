import numpy as np

def rgb(minimum, maximum, value):
    if value < minimum or value > maximum:
        print(minimum, maximum, value)
    minimum, maximum = float(minimum), float(maximum)
    ratio = 2 * (value-minimum) / (maximum - minimum)
    b = int(max(0, 255*(1 - ratio)))
    r = int(max(0, 255*(ratio - 1)))
    g = 255 - b - r
    return r, g, b

def mandel_rgb(val, max_iter):
    if val == max_iter-1:
        return (0, 0, 0)
    else:
        return rgb(1, max_iter, max_iter-val)

def pos_to_complex(x, y):
    return x + y * (-1)**0.5

def mandel_iterator(val, max_iter):
    cur_val = 0
    for i in range(max_iter):
        iterations = i
        cur_val = cur_val ** 2 + val 
        if abs(cur_val) > 2:
            break
    return iterations


def calc_value(max_iter, px_width=800, px_height=600, center_point=(0, 0), pixel_to_value_ratio=200):
    vals = np.empty((px_width, px_height), dtype=object) 
    half_width_in_val = px_width / pixel_to_value_ratio / 2
    half_height_in_val = px_height / pixel_to_value_ratio / 2
    # converts pixel coordinates to x and y axis coordinates
    for x in range(px_width):
        for y in range(px_height):
            x_as_val = x / pixel_to_value_ratio - half_width_in_val + center_point[0]
            y_as_val = -y / pixel_to_value_ratio + half_height_in_val + center_point[1]
            vals[x, y] = (x_as_val, y_as_val)
    
    # converts coordinates to complex values
    for x in range(px_width):
        for y in range(px_height):
            vals[x, y] = pos_to_complex(*vals[x, y])


    # does mandelbrot iteration and maps to a color
    for x in range(px_width):
        for y in range(px_height):
            vals[x, y] = mandel_rgb(mandel_iterator(vals[x, y], max_iter), max_iter)
    return vals

def pixel_to_real(x, y, px_width=800, px_height=600, center_point=(0, 0), pixel_to_value_ratio=200):
    half_width_in_val = px_width / pixel_to_value_ratio / 2
    half_height_in_val = px_height / pixel_to_value_ratio / 2
    x_as_val = x / pixel_to_value_ratio - half_width_in_val + center_point[0]
    y_as_val = -y / pixel_to_value_ratio + half_height_in_val + center_point[1]
    return (x_as_val, y_as_val)

if __name__ == "__main__":
    calc_value(0)