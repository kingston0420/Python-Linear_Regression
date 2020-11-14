#Linear Regression is when you have a group of points on a graph, and you find a line that approximately resembles that group of points. A good Linear Regression algorithm minimizes the error_, or the distance from each point to the line. A line with the least error is the line that fits the data the best. We call this a line of _best fit.
#This code create a function that will find a line of best fit when given a set of data.
"""The line we will end up with will have a formula that looks like:
y = m*x + b
m is the slope of the line and b is the intercept, where the line crosses the y-axis."""

#get the y value based on m,b,x
def get_y(m, b, x):
    y = m*x + b
    return y

#take in m, b, and an [x, y] point called point and return the distance between the line and the point.
def calculate_error(m, b, point):
    x_point, y_point = point
    return abs(get_y(m, b, x_point)-y_point)


#takes m and b that describe a line, and points, a set of data and iterate through each point in points and calculate the error from that point to the line (using calculate_error). It should keep a running total of the error, and then return that total after the loop.
def calculate_all_error(m, b, points):
    total_error = 0
    for point in points:
        total_error += calculate_error(m, b, point)
    return total_error    

#find the best fit line
def main():
    possible_ms = [m*0.1 for m in range(-100, 101)]
    possible_bs = [b*0.1 for b in range(-200, 201)]    
    datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
    smallest_error = float("inf")
    best_m = 0
    best_b = 0
    for m in possible_ms:
        for b in possible_bs:
            error = calculate_all_error(m, b, datapoints)
            if error < smallest_error:
                best_m = m
                best_b = b
                smallest_error = error
    print(best_m, best_b, smallest_error)

#now we can use get_y() with the best_m and best_b to predict the output y with a given x 