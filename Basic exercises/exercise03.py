def highest_value(temperatures):
    highest = temperatures[0]
    for h in temperatures:
        if h > highest:
            highest = h
    return highest

def lowest_value(temperatures):
    lowest = temperatures[0]
    for l in temperatures:
        if l < lowest:
            lowest = l
    return lowest

def above_17(temperatures):
    count = 0
    for i in temperatures:
        if i > 17:
            count += 1
    return count

temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]
print("Wednesday:", temperatures[2])
print("Max:", highest_value(temperatures))
print("Min:", lowest_value(temperatures))
print("Average:", round(sum(temperatures)/len(temperatures), 1))
print("Days above 17:", above_17(temperatures))
print("Sorted:", sorted(temperatures))