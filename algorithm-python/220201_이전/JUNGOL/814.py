m = int(input())

# 평년의 경우 1월부터 12월까지 일수는 각각 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31일이다.

arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(arr[m-1])