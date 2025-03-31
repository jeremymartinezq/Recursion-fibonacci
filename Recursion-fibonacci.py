# Python program to
# demonstrate recursion with Fibonacci series

# Function for fibonacci
def fib(n):

    # Base case 1
    if (n == 0):
        return 0

    # Base case 2
    if(n == 1 or n == 2):
        return 1

    # Recursion function
    else:
        return (fib(n - 1) + fib(n - 2))

    # Driver Code
    # Initiate variable n.
    n = 5
    print("Fibonacci series of 5 numbers is:", end=" ")
    # for loop to print the fibonacci series
    for i in range(0,n):
        print(fib(i), end=" ")
        done
