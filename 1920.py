'''
작성자 : 서현

작성일자 : 2022.03.14

작성내용 : N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다.
다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

todo :
1) A의 배열을 입력받아 오름차순 정렬을 한다.
2) 비교를 할 입력값을 B 리스트에 입력받는다.
3) B의 값이 A 리스트에 있는지 하나씩 확인을 하되 시작점과 끝점의 중간 값부터 비교를 하며 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인하고 
중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인한다.
4) B의 값이 A 리스트에 있으면 1을 없으면 0을 출력하게 한다.

'''
import sys

# 이진 탐색
def binary_search(array, target, start, end):
    while start <= end:
        # 시작점과 끝점의 중간 값
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

N = int(input())

#A의 배열을 입력받아 오름차순 정렬을 한다.
A = list(map(int, sys.stdin.readline().split()))
A.sort()

M = int(input())
#비교를 할 입력값을 B 리스트에 입력받는다.
B = list(map(int, sys.stdin.readline().split()))

#B의 값이 A 리스트에 있는지 하나씩 확인을 하고 있으면 1을 없으면 0을 출력하게 한다.
for i in B:

    result = binary_search(A, i, 0, N - 1)
    if result != None:
        print(1)
    else:
        print(0)
