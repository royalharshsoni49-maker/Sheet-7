def power(n):
    if n == 0:
        return 1
    return n * power(n*n,n=0)
n=int(input("ENTER A NUMBER :"))
print(power(n)
