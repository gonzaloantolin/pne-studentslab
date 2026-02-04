def fibosum(n):
    a = 0
    b = 1
    lst = []
    for i in range(n):
        lst.append(a)
        a, b = b, a + b
        i += 1
    return lst

print("The sum of the first 5 elements of the Fibonacci series is:", sum(fibosum(6)))
print("The sum of the ten first elements of the fibonacci series is: ", sum(fibosum(11)))