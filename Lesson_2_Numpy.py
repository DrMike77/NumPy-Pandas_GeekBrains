import numpy as np
x = np.array([[1,2,3,3,1],[6,8,11,10,7]])
a = np.matrix.transpose(x)
print(a)
print(f' Массив ', np.mean(a, axis = 0))
average = np.mean(a, axis = 0)
a_centered = a-average
print(f' Массив ', type(a_centered), a_centered)
v1 = a_centered[0:,0]
v2 = a_centered[0:,1]
a_centered_sp = v1.dot(v2)
print(f'Скалярное произведение признаков:', a_centered_sp)
N = a_centered.shape[0]
print(f'a_centered_sp / (N-1) = ', a_centered_sp / (N-1))
cov_matrix = np.cov(x)
print(f'Ковариационная матрица:', cov_matrix,f'Значение ковариации =',cov_matrix[0,1])
