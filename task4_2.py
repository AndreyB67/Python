# Написать два алгоритма нахождения i-го по счёту простого числа. Первый - использовать
# алгоритм решето Эратосфена.
# Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.
import cProfile

# Вариант 1. Решето Эратосфена.

def sieve(num_list, idx):
    num_list[1] = 0
    i = 2
    s_num_list = []
    while len(s_num_list) < idx:
        if num_list[i] != 0:
            s_num_list.append(num_list[i])
            j = i * 2
            while j < len(num_list):
                num_list[j] = 0
                j += i
        i += 1
    return s_num_list[-1]

y = 2000
x = [i for i in range(y * y)]
cProfile.run('sieve(x, y)')

# для 1000
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.515    1.515 <string>:1(<module>)
#         1    1.102    1.102    1.515    1.515 task_4_2.py:9(sieve)
#         1    0.000    0.000    1.515    1.515 {built-in method builtins.exec}
#   2464833    0.413    0.000    0.413    0.000 {built-in method builtins.len}
#      1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          8923 function calls in 0.066 seconds

#"""
#для 2000
 #         10181972 function calls in 6.999 seconds
 #
 #   Ordered by: standard name
 #
 #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #        1    0.000    0.000    6.999    6.999 <string>:1(<module>)
 #        1    5.280    5.280    6.999    6.999 task_4_2.py:9(sieve)
 #        1    0.000    0.000    6.999    6.999 {built-in method builtins.exec}
 # 10179968    1.718    0.000    1.718    0.000 {built-in method builtins.len}
 #     2000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
 #        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


# Вариант 2. Перебор.

def simple_num(num_list, idx):
    num_list[1] = 0
    s_nums = []
    for i in range(2, len(num_list)):
        for num in s_nums:
            if num_list[i] % num == 0:
                break
        else:
            s_nums.append(num_list[i])
        if len(s_nums) == idx:
            return s_nums[-1]

y = 2000
x = [i for i in range(y * y)]
cProfile.run('simple_num(x, y)')

"""
#для 1000
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.066    0.066 <string>:1(<module>)
#         1    0.064    0.064    0.066    0.066 task_4_2.py:29(simple_num)
#         1    0.000    0.000    0.066    0.066 {built-in method builtins.exec}
#      7919    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#      1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#"""
#для 2000
   #       19393 function calls in 0.330 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.329    0.329 <string>:1(<module>)
   #      1    0.326    0.326    0.329    0.329 task_4_2.py:41(simple_num)
   #      1    0.000    0.000    0.330    0.330 {built-in method builtins.exec}
   #  17389    0.003    0.000    0.003    0.000 {built-in method builtins.len}
   #   2000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#"""
#print(f'Внутри 1 способа время выполнения выросло {round(1.718/0.43,2)}')
#print(f'Внутри 2 способа время выполнения выросло {round(0.326/0.064,2)}')
#print(f'по сравнению друг с другом время выполнения по решету сотносится {round(1.718/0.43,2)}')
#print(f'по сравнению друг с другом время выполнения по решету сотносится {round(0.43/0.064,2)}')
# Внутри 1 способа время выполнения выросло в 4.0
# Внутри 2 способа время выполнения выросло в 5.09
#По сравнению друг с другом время выполнения по решету больше в 4.0
#По сравнению друг с другом время выполнения по решету больше в 6.72


#"""