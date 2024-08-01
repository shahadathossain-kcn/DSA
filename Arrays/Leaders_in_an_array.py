arr = [16, 17, 18, 3, 5, 165,12]
n = len(arr)

max_right = arr[-1]
print(max_right)

for i in range(n-2 , -1, -1):
    if arr[i] > max_right:
        print(arr[i])
        max_right = arr[i]
