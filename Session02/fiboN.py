def fibonacci(n):
    a = 0
    b = 1
    lst = []
    for i in range(n):
        lst.append(a)
        a, b = b, a + b
        i += 1
    return lst

lst = fibonacci(16)
print("The fifth element of the fibonacci series is:", lst[5])
print("The tenth element of the fibonacci series is:", lst[10])
print("The fifteenth element of the fibonacci series is:", lst[15])

