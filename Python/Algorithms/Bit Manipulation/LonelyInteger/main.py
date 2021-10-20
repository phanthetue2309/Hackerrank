n = input()
arr = list(map(int, input().split()))
arr.sort()
for i in range(1, len(arr)-1):
    if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
        print(arr[i])
        break
    if i == len(arr)-2:
        print(arr[i+1])