import numpy as np
a = np.array([[1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7]])
print("Размер/форма a: {}".format(a.shape), "\nРазмерность a: {}".format(a.ndim))

mean_a = a.mean(axis=0)
print("Среднее значение по столбцам = {}".format(mean_a))



