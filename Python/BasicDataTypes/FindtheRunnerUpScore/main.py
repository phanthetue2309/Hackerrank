if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr.reverse()
    for i in arr: 
        if i == max(arr) :
            continue
        else :
            print(i)
            break
        