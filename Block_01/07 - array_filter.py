import sys
sys.path.append("..")
import useful_functions as useful


original = useful.random_array(-200, 200, 100)

# В первом массиве - оставить только чётные положительные числа.
pos_even_array = list(filter(lambda a: (a % 2 == 0 and a > 0), original))

# Во втором массиве - оставить только двузначные числа, кратные 10. В обоих случаях для фильтрации используем lambda-функции.
div_ten_array = list(filter(lambda x: (x % 10 == 0 and abs(x) % 100 == abs(x) and x != 0), original))

print("\nOriginal Array = ", end="")
useful.print_array(original)

print("\nFirst Array = ", end="")
useful.print_array(pos_even_array)

print("\nSecond Array = ", end="")
useful.print_array(div_ten_array)