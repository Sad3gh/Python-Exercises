def fibonacci_sequence(n):
    #returning an empty list when n is equal or less than 0
    if n <= 0:
        return []
    #handling the cases which n is less than 2
    if n == 1:
        return [0]
    if n ==2:
        return [0,1]
    sequence = [0, 1] #assigning the first two numbers of the sequence
    #generating new values for the sequence up to the n(th) element
    for i in range(2,n):
       next_value =  sequence[i-1] + sequence[i-2]
       sequence.append(next_value)

    return sequence

#test cases
print(fibonacci_sequence(10))
print(fibonacci_sequence(5))
print(fibonacci_sequence(12))