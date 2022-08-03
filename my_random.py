import time

import numpy as np


class MyRandom:

	def __init__(self):
		self.time: int = int(time.time() * 1000)  # Получение текущего времени.
		str_time = str(self.time)
		str_time = str_time[len(str_time) - 4:len(str_time)]
		self.seed: int = int(str_time)

	def reload_params(self):
		self.time = int(time.time() * 1000)  # Получение текущего времени.

	# Генерация числа в диапазоне [0, 1)
	def rand(self):
		# Xn = (aX(n-1) + c) mod m
		a = 1140671485
		c = 128201163
		m = 2 ** 24
		self.seed = (a * self.seed + c) % m
		return self.seed / m

	# Генерация случайного числа в заданном диапазоне
	def rand_in_range(self, _min, _max):
		_max -= _min
		return (self.rand() * ++_max) + _min

	# Создание массива случайных значений в заданном диапазоне
	def rand_range(self, _min, _max, count):
		x = np.zeros(count)
		for i in range(count):
			x[i] = self.rand_in_range(_min, _max)

		return x