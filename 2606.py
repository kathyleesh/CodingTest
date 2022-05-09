'''
작성자 : 서현

작성일자 : 2022.05.08

작성내용 : 
* 문제 : 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
        예를 들어 7대의 컴퓨터가 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 
        2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.
        어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 
        출력하는 프로그램을 작성하시오.

* 입력 : 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의
         수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

* 출력 : 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

* 예제 : 입력                       출력
       --------------------     -----------
        7                         4
        6
        1 2
        2 3
        1 5
        5 2
        5 6
        4 7

todo : 1) 컴퓨터의 수를 입력 받은 다음 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수를 입력 받는다.
       2) 그 수만틈 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍을 입력받는다.
       3) 컴퓨터끼리 연결되어있는 집합을 찾고 부모 노드를 연결시킨다.
       4) 부모 노드가 1인(바이러스에 감염된) 컴퓨터의 개수를 센다.
'''

import sys
# 특정 노드가 속한 집합을 찾기


def find(parent, x):
    # 루트 노드를 찾을 때까지 재귀호출
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기(부모노드 설정)


def union_parent(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 컴퓨터 수와 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수를 입력받는다.
Computer = int(input())
Connect = int(input())

# 네트워크를 초기화한다.
infection = [0]*(Computer+1)

# 네트워크 상에서 부모를 자기 자신으로 초기화한다.
for i in range(1, Computer+1):
    infection[i] = i

# Union 연산을 각각 수행
for i in range(Connect):
    a, b = map(int, sys.stdin.readline().split())
    union_parent(infection, a, b)

infected = 0
# infection list 값이 1인 index는 바이러스에 감염이 된 컴퓨터이므로 그 수를 센다.
for i in range(1, Computer+1):
    if find(infection, i) == 1:
        infected += 1

# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력한다.
print(infected-1)