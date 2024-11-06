def prime_factorization(n):
    factors = []

    #check for the number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # n must be odd  at this point, so we can check only odd numbers from now on
    for i in range(3, int(n**.05)+ 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    # after all this, this condition is to check if n itself is a prime number greater than 2
    if n > 2:
        factors.append(n)

    return factors

def main():
    number = int(input("Enter a number to factor: "))

    if number <= 1:
        print("Please Enter a number greater than 1")
        return
    factors = prime_factorization(number)
    print(f"Prime factorization of {number} is: {','.join(map(str,factors))}")

if __name__ == "__main__":
    main()
