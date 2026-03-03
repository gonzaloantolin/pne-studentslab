def fibonacci():
    a = 0
    b = 1
    count = 0
    while count < 11:
        print(a, end=" ")
        a, b = b, a + b
        count += 1

fibonacci()

