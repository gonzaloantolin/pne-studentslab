def letter_grade(n):
    if 0.0 <= n <= 2.9:
        result = "F"
    elif 3.0 <= n <= 4.9:
        result = "D"
    elif 5.0 <= n <= 6.9:
        result = "C"
    elif 7.0 <= n <= 8.9:
        result = "B"
    elif 9.0 <= n <= 10.0:
        result = "A"
    else:
        return "ERROR"
    return result

print("Score", 9.5, "->", letter_grade(9.5))
print("Score", 7, "->", letter_grade(7))
print("Score", 5.5, "->", letter_grade(5.5))
print("Score", 3.2, "->", letter_grade(3.2))
print("Score", 1.0, "->", letter_grade(1.0))



