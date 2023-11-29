import math
import random as rnd
import pandas as pd
import matplotlib.pyplot as plt


def randomXY():
    x = rnd.uniform(-1, 1)
    y = rnd.uniform(-1, 1)
    return x, y


def monteCarlo(n):
    M = 0
    for i in range(n):
        x, y = randomXY()
        if (x ** 2 + y ** 2) <= 1:
            M += 1
    pi = 4 * (M / n)
    return pi


arr = []
num = []
sigma = []
for N in range(100, 5000, 100):
    x = monteCarlo(N)
    pi = math.pi
    arr.append(x)
    num.append(N)
    sigma.append((1 - (x / pi)) * 100)

plt.subplot(1, 3, 1)
plt.plot(num, arr, marker='o', markersize=5)
plt.hlines(math.pi, 0, 5000, color='red')
plt.xlabel("Кол-во испытаний")
plt.ylabel("Значение ПИ")
plt.title("График №1")

plt.subplot(1, 3, 3)
plt.plot(num, sigma, marker='o', markersize=5)
plt.hlines(0, 0, 5000, color='blue')
plt.xlabel("Кол-во испытаний")
plt.ylabel("Отклонение в %")
plt.title("График №2")
data = pd.DataFrame({'Кол-во испытаний': num, 'Значение PI': arr, 'Отклонение в процентах': sigma})
print(data)
plt.show()
