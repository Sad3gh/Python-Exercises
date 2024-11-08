def prime_checker(n):
    #Check for number less than or equal to 1
    if n <= 1:
        return False
    # 2 is a prime number(the only even number that is prime)
    if n == 2:
        return True
    #Every even number greater than 2 is NOT a prime number
    if n % 2 ==0:
         return False
    #Checking for the presence of any odd factor so we can falsify the number of being Prime
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    #After ensuring that there's no divisor,we can finally be sure that our number is Prime
    return True

#test cases
print(prime_checker(14))