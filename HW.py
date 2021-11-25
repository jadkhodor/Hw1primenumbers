print('Enter the N prime numbers you would like to find:')
x = input()
x = int(x)
n = 2
while x!= 0:
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n)
        x-= 1
    n+= 1