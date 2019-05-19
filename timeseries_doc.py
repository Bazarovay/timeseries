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


def smooth_with_ewma(data, alpha=None,future_steps=None):
    """ Smooth using moving average. Adds None for nonexistent values """
    ewma_ma = exponential_moving_average(data, alpha=alpha,future_steps=future_steps)
    ewma_ma = [None] + ewma_ma
    return ewma_ma

def centered_moving_average(data):
    """
    Centered average
    Smoothing the smoothed value
    """
    avg = get_moving_average(amount, steps=4)
    avg = get_moving_average(avg, steps=2)
    return avg

def double_exponential_moving_average(data, alpha=None, gamma=None,future_steps=None):
    """
    St = a*yt_1 + (1 - a)*(St_1 + bt_1)
    """
    # initializing
    weighted_array = [data[0]]
    beta_array = [((data[1]-data[0]) + (data[2]-data[1]) + (data[3]-data[2]))/3]
    forecast = [weighted_array[0] + beta_array[0]]
    for el in data[1:]:
        weighted_obs = alpha*el + (1 - alpha)*(weighted_array[-1] + beta_array[-1])
        weighted_array.append(weighted_obs)
        beta_obs = gamma*(weighted_array[-1] - weighted_array[-2]) + (1 - gamma)*beta_array[-1]
        beta_array.append(beta_obs)
        forecast.append(weighted_obs + beta_obs)

    if future_steps:
        for step in range(1,future_steps + 1):
            weighted_obs = forecast[-1] + step*beta_array[-1]
            forecast.append(weighted_obs)

    return forecast


def exponential_moving_average(data, alpha=None, future_steps=None):
    """
    Exponential moving average
    St = a*yt_1 + (1 - a)*St_1
    St = a yt-1 + (1 - a) [ayt-2 + (1 - a)St-2]
    Multiply smoothing parameter with the last value.
    Multiple (1-a) with previous weighted observation
    St = a*yt_1 + a(1-a)*yt_2 + (1-a)^2St_2
    St =
    """
    if alpha > 1 or alpha < 0:
        raise ValueError("alpha has to be between 0 and 1")

    alpha_min_1 = 1 - alpha


    i = 1
    weighted_array = []
    while i < len(data):
        weighted = 0
        k = 0
        while (i - k - 1) >= 1: # multiply past observations with the smoothing parameter
            weighted += alpha_min_1**(k)*data[i - k - 1] #  (1-a)^k*yt_1 ...
            k = k + 1

        weighted = alpha*weighted
        weighted += alpha_min_1**(i - 1)*data[0]

        weighted_array.append(weighted)
        i = i + 1

    if future_steps:
        constant_origin = data[-1]
        for step in range(1,future_steps + 1):
            weighted_obs = alpha*constant_origin + alpha_min_1*weighted_array[-1]
            weighted_array.append(weighted_obs)


    return weighted_array
#
# if __name__ == "__main__":
#     supplier = [x for x in range(1,13)]
#     # random
#     amount = [9, 8, 9, 12, 9, 12, 11]#, 7, 13, 9, 11, 10]
#     # trend
#     # amount = [x for x in range(10,130,10)]
#
#     # average = get_average(amount)
#     # error_per_amount = [squared_error(actual,average) for actual in amount]
#     # mse = mean_squared_error(error_per_amount)
#     # print(mse)
#
#
#     # average = smooth_with_moving_average(amount, steps=5)
#     #
#     # plt.plot(amount, 'r', average, 'b')
#     # plt.ylabel('Actual and Predicted')
#     # plt.show()
#
#     yt = [71, 70, 69, 68, 64, 65, 72, 78, 75, 75, 75, 70]
#     final_exponential_average = None
#     final_alpha = None
#     min_mse = 1000
#     for a in [.1,.2,.3,.4,.5,.6,.7,.8,.9,1]:
#         exponential_average = smooth_with_ewma(yt, alpha=a)
#
#         all_errors = []
#         for i, val in enumerate(yt):
#             if exponential_average[i]:
#                 error_val = squared_error(yt[i],exponential_average[i])
#                 all_errors.append(error_val)
#
#         mse = mean_squared_error(all_errors)
#
#
#         if not final_exponential_average:
#             final_exponential_average = exponential_average
#             min_mse = mse
#             final_alpha = a
#         elif mse < min_mse:
#             final_exponential_average = exponential_average
#             min_mse = mse
#             final_alpha = a
#
#
#     plt.plot(yt, 'r', final_exponential_average, 'b')
#     plt.ylabel('Actual and Predicted for alpha {}'.format(final_alpha))
#     plt.show()


new_y = [6.4,  5.6,  7.8,  8.8,  11,  11.6,  16.7,  15.3,  21.6,  22.4]
dwema = double_exponential_moving_average(new_y,alpha=0.3623,gamma=1.0,future_steps=5)

swema = smooth_with_ewma(new_y, alpha=.977,future_steps=5)

plt.plot(new_y, 'r', dwema, 'b^',swema,'g--')
plt.legend(["Actual","Double Exponential", "Single Exponential"])
plt.ylabel('Actual and Predicted')
plt.show()
