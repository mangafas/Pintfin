from statistics import mean
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

df = pd.read_csv("aapl.csv")


xs = np.array(df["id"], dtype=np.float64)
ys = np.array(df["change"], dtype=np.float64)


def best_fit_slope_and_intercept(xs, ys):
    m = (((mean(xs) * mean(ys)) - mean(xs * ys)) /
         ((mean(xs) * mean(xs)) - mean(xs * xs)))

    b = mean(ys) - m * mean(xs)

    return m, b


m, b = best_fit_slope_and_intercept(xs, ys)

regression_line = [(m*x)+b for x in xs]


style.use('ggplot')
plt.scatter(xs,ys,color='#003F72')
plt.plot(xs, regression_line)
plt.show()

predict_x = 147
predict_y = (m*predict_x)+b
print(predict_y)
