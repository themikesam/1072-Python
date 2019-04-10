import math
def meanStddev(data) :
    sum = 0
    for x in data :
        sum = sum + x
    avg = sum / len(data)
    sum = 0
    for x in data:
        sum = sum + (-avg)*(x-avg)
    dev = math.sqrt(sum/len(data))
    return avg, dev

def main()
    # input int n
    n = int(input())
    # then input n int
    data = list()
    for i in range(n) : # 0 <= i < n
        data.append(int(input()))
    # cal mean and stddev of all inputs
    mean, std = meanStddev(data)
    print(mean, std)
main()