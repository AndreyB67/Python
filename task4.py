"""Определить, какое число в массиве встречается чаще всего"""
from random import random

N = 13
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * N)
print(arr)

num = arr[0]
max_freq = 1
for i in range(N - 1):
    freq = 1
    for j in range(i + 1, N):
        if arr[i] == arr[j]:
            freq += 1
    if freq > max_freq:
        max_freq = freq
        num = arr[i]

if max_freq > 1:
    print(max_freq, 'раз встречается число', num)
else:
    print('Все элементы уникальны')