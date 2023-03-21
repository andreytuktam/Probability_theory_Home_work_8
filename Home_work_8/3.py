import math

# Известно, что рост футболистов в сборной распределен нормально с дисперсией 
# генеральной совокупности, равной 25 кв.см. Объем выборки равен 27, среднее 
# выборочное составляет 174.2. Найдите доверительный интервал для математического 
# ожидания с надежностью 0.95.

l = 174.2 - 1.96 * (25 / math.sqrt(27)) 
r = 174.2 + 1.96 * (25 / math.sqrt(27)) 
print(l, r)