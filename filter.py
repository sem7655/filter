def f(a):
    if a % 2 == 0:
        return a
a = filter(f, (2, 4, 6, 7, 9, 0))# фильтруем числа
print(list(a))
