n = int(input("Ввести число"))
i = 0
for i in range(n):
   i=i+1
   print('*' * i)


n = int(input("Ввести число"))
i = 0
for i in range(n):
    i=i+1
    print(' ' * (n-i),'*' * i)


n = int(input("Ввести число"))
i = 0
for i in range(n):
    print('*' * n)
    n -= 1

n = int(input("Ввести число"))
i = 0
for i in range(n):
    i=i+1
    print(' ' * i, '*' * n )
    n -= 1