import time;  # 引入time模块

def isPrime(n):
    # prime numbers are greater than 1
    if n > 1:
        # check for factors
        for i in range(2,n):
            if (n % i) == 0:
                print(n,"不是質數")
                print(i,"x",n//i,"=",n)
                break
            else:
                print(n,"是質數")
                break
    # if input nber is less than
    # or equal to 1, it is not prime
    else:
        print(n,"不是質數")

def isPrime_ans(n):
    i = 2
    if n > 1:
        while i < n:
            if n % i == 0:
                return False
            i+=1
        return True
    else:
        return False

def sumPrime(n):
    i = 0
    sum = 0
    while i < n:
        i+=1
        if(isPrime_ans(i)):
            sum+=1
    return sum

def Main():
    start = time.time()
    n = int(input())
    print(sumPrime(n))
    end = time.time()
    print('共用了',(end-start)*1000,'ms')

Main()