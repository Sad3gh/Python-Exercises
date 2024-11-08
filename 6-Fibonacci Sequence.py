def fibonacci_sequence(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n ==2:
        return [0,1]
    sequence = [0, 1]
    for i in range(2,n):
       next_value =  sequence[i-1] + sequence[i-2]
       sequence.append(next_value)

    return sequence

print(fibonacci_sequence(10))
print(fibonacci_sequence(5))
print(fibonacci_sequence(12))