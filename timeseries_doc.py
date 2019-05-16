# Supplier 	Amount 	Supplier 	Amount
# 1 	9 	7 	11
# 2 	8 	8 	7
# 3 	9 	9 	13
# 4 	12 	10 	9
# 5 	9 	11 	11
# 6 	12 	12 	10
import matplotlib.pyplot as plt

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

def mean(data):
    """
    Return data mean
    """
    return sum(data)/len(data)

supplier = [x for x in range(1,13)]
amount = [9, 8, 9, 12, 9, 12, 11, 7, 13, 9, 11, 10]

average = mean(amount)

error_per_amount = [squared_error(actual,average) for actual in amount]

mse = mean_squared_error(error_per_amount)
print(mse)

plt.show()
