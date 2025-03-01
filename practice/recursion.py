def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

def fibonaci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonaci(n-1) + fibonaci(n-2)

# print(fact(5))
# print(fibonaci(5),end = " ")
for i in range(5):
    print(fibonaci(i),end = " ")
