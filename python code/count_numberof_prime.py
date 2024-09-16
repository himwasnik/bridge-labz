def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
             return True
        else:
             return False

def prime(numbers):
    primenumbers = []
    for x in numbers:
        if is_prime(x):
            primenumbers.append(x)
   
    return len(primenumbers)

num = [1, 2, 3, 4, 5, 6, 7, 98, 9, 8, 57, 55]
ans = prime(num)
print(ans)