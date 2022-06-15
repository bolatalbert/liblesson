import numpy as np
a = np.array([[1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7]], dtype=float)
print("Размер/форма a: {}".format(a.shape), "\nРазмерность a: {}".format(a.ndim))

mean_a = a.mean(axis=0, dtype=float)
print("Среднее значение по столбцам = {}".format(mean_a))

# задание 2
a_centered = a - mean_a
print("Массив a минус среднее значение массива a = {}".format(a_centered))
print("Размер/форма: {}".format(a_centered.shape), "\nРазмерность: {}".format(a_centered.ndim))

# Задание 3
print("Первый столбец: {}".format(a[0:, 0]))
print("Второй столбец: {}".format(a[0:, 1]))
c = a[0:,0].copy()
b = a[0:,1].copy()
print("Произведение первого столбца на второй = : {}".format(c*b))

#конец


