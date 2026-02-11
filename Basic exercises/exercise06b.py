def classify_triangle(a, b, c):
    if a == b == c:
        result = "equilateral"
    elif a == b or b == c or a == c:
        result = "isosceles"
    elif a != b != c:
        result = "scalene"
    return result

print("classify_triangle(5, 5, 5) =", classify_triangle(5, 5, 5))
print("classify_triangle(5, 5, 5) =", classify_triangle(3, 3, 4))
print("classify_triangle(5, 5, 5) =", classify_triangle(3, 4, 5))