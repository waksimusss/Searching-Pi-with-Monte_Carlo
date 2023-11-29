# Задание A1 Максимов Никита БПИ 227-1
## [Код прогрaммы](main.py)
```python
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
```
## Выводы и результаты

![Результаты](https://github.com/waksimusss/Searching-Pi-with-Monte_Carlo/assets/113054845/dd57fa4c-d2c4-4bea-bbda-67596ea31b97)

| Кол-во испытаний | Значение PI | Отклонение в процентах|
| --- | --- | --- |
| 100 | 3.400000 | -8.225361 |
| 200 | 3.080000 |  1.960555 |
| 300 | 3.053333 |  2.809381 |
| 400 | 3.210000 | -2.177473 |
| 500 | 3.296000 | -4.914938 | 
| 600 | 3.186667 | -1.434750 |     
| 700 | 3.148571 | -0.222141 |   
| 800 | 3.260000 | -3.769023 |   
| 900 | 3.222222 | -2.566519 |   
| 1000 | 3.128000 | 0.432668  |                                     
| 1100 | 3.207273 | -2.090662 | 
| 1200 | 3.106667 | 1.111729 | 
| 1300 | 3.196923 | -1.761222 | 
| 1400 | 3.174286 | -1.040652 | 
| 1500 | 3.133333 | 0.262902 | 
| 1600 | 3.137500 | 0.130273 | 
| 1700 | 3.152941 | -0.361235 | 
| 1800 | 3.146667 | -0.161511 | 
| 1900 | 3.067368 | 2.362631 | 
| 2000 | 3.170000 | -0.904234 | 
| 2100 | 3.095238 | 1.475511 | 
| 2200 | 3.083636 | 1.844806 | 
| 2300 | 3.114783 | 0.853390 | 
| 2400 | 3.130000 | 0.369006 | 
| 2500 | 3.187200 | -1.451727 | 
| 2600 | 3.135385 | 0.197608 | 
| 2700 | 3.155556 | -0.444453 | 
| 2800 | 3.100000 | 1.323935 | 
| 2900 | 3.140690 | 0.028743 | 
| 3000 | 3.124000 | 0.559992 | 
| 3100 | 3.136774 | 0.153376 | 
| 3200 | 3.126250 | 0.488372 | 
| 3300 | 3.173333 | -1.010337 | 
| 3400 | 3.137647 | 0.125592 | 
| 3500 | 3.176000 | -1.095220 | 
| 3600 | 3.168889 | -0.868866 | 
| 3700 | 3.148108 | -0.207393 | 
| 3800 | 3.121053 | 0.653809 | 
| 3900 | 3.140513 | 0.034372 | 
| 4000 | 3.163000 | -0.681417 | 
| 4100 | 3.108293 | 1.059971 | 
| 4200 | 3.128571 | 0.414478 | 
| 4300 | 3.110698 | 0.983418 | 
| 4400 | 3.137273 | 0.137508 | 
| 4500 | 3.162667 | -0.670807 | 
| 4600 | 3.138261 | 0.106054 | 
| 4700 | 3.122553 | 0.606045 | 
| 4800 | 3.170833 | -0.930760 | 
| 4900 | 3.175510 | -1.079629 | 
| 5000 | 3.160800 | -0.611389 | 

Перед расуждаениями, стоит отметить, что данные кадждый раз получаются новыми, все-таки точки генерируются каждый раз случайным образом. Я привел пример получившихся результатов после выполнения программы. На их основе сделаем общие выводы. Как можно заметить, с увеличение кол-ва испытаний стретимиться к максимально точному числу. При этом необходится и без выбросов даже на большом кол-во испытаний, просто многоие точки попадают не вокуржность, но шанс этого все уменьшается и уменьшается при увеличнении кол-во тестов. это можон проверить, запустив программу на с очень болшим N 
> Я изменил цикл и проходился от 100 до 200000 с шагом в 10000.





