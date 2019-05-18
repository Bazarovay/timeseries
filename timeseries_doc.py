# Supplier 	Amount 	Supplier 	Amount
# 1 	9 	7 	11
# 2 	8 	8 	7
# 3 	9 	9 	13
# 4 	12 	10 	9
# 5 	9 	11 	11
# 6 	12 	12 	10
import matplotlib.pyplot as plt
import numpy as np

def squared_error(actual, predicted):
    """
    Squared error
    """
    sse = (actual - predicted)**2
    return sse

def mean_squared_error(errors):
    """
    Return mean squared error
    """
    mse = sum(errors)/len(errors)
    return mse

def get_average(data):
    """
    Return data mean
    """
    return sum(data)/len(data)

def plot(actual,predicted):
    """
    Plot actual and predicted values
    """
    average_line = np.array([predicted for i in range(len(actual))])

    plt.plot(actual, 'r', average_line, 'b')
    plt.ylabel('Actual and Predicted')
    # plt.xlabel('')

    plt.show()

def get_moving_average(data, steps=2):
    """
    Return moving average
    """
    moving_average = []
    for i in range(0,len(data) - steps + 1):
        data_window = data[i:i + steps]
        avg = get_average(data_window)
        moving_average.append(avg)

    return moving_average

def smooth_with_moving_average(data, steps=2):
    """ Smooth using moving average. Adds None for nonexistent values """
    moving_average = get_moving_average(data, steps=2)
    moving_average = [None]*steps + moving_average
    return moving_average


def centered_moving_average(data):
    """
    Centered average
    Smoothing the smoothed value
    """
    avg = get_moving_average(amount, steps=4)
    avg = get_moving_average(avg, steps=2)
    return avg

def exponential_moving_average(data, alpha=None):
    """
    Exponential moving average
    St = a yt-1 + (1 - a) [ayt-2 + (1 - a)St-2]
    Multiply smoothing parameter with the last value.
    Multiple (1-a) with previous weighted observation
    """"



supplier = [x for x in range(1,13)]
# random
amount = [9, 8, 9, 12, 9, 12, 11]#, 7, 13, 9, 11, 10]
# trend
# amount = [x for x in range(10,130,10)]

# average = get_average(amount)
# error_per_amount = [squared_error(actual,average) for actual in amount]
# mse = mean_squared_error(error_per_amount)
# print(mse)


# average = smooth_with_moving_average(amount, steps=5)
#
# plt.plot(amount, 'r', average, 'b')
# plt.ylabel('Actual and Predicted')
# plt.show()


print(avg)
