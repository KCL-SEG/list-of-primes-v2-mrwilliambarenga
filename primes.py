"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    
    if number_of_primes <= 0:
        raise ValueError(f"Input = {number_of_primes} should have been greater than or equal to 1")

    list = [2]
    number = 3
    count = 1

    while count < number_of_primes:
        
        for x in list:

            if number%x == 0:
                break
        else:
            list.append(number)
            count += 1

        number += 1


    return list
