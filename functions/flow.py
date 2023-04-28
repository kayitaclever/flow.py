# Write a function that uses while, if and continue statements to print all 
# the even numbers between 0 and 50. 

def even_numbers():
    x=1
    while x<50:
        x+=1
        if x%2!=0:
            continue
        print(x)

# Write a function that takes an integer argument and prints "Prime" if th
# e number is prime, and "Not prime" if the number is not prime.


# def is_prime_number(x):
#     x>1
#     for i in range(2,x,+ 1):
#         if x%i ==0:
#             print("Prime")
         
#         else:
#             print("not prime")

    def check_prime(n):
        if n <= 1:
            print("Not prime")
        return
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                 print("Not prime")
            return
    print("Prime")        
            
    
        # Write a function that takes a list of integers as input and prints the sum of all the even 
    # numbers in the list.

    def sum_even_numbers(numbers):
        sum = 0
        for num in numbers:
            if num % 2 == 0:

                 sum += num
        print("The sum of even numbers in the list is:", sum)

        # Write a function that takes any two integers as input, and prints the sum of all the numbers 
        # between the two integers (inclusive) that are divisible by 3.


def sum_numbers_divisible_by_three(num1, num2):
    sum = 0
    for num in range(num1, num2+1):
        if num % 3 == 0:
            sum += num
    print("The sum of all numbers between", num1, "and", num2, "that are divisible by 3 is:", sum)





