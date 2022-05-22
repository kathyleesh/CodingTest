'''
작성자 : 서현

작성일자 : 2022.05.09

작성내용 : 
* 문제 : 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

* 입력 : 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 
        둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

* 출력 : 첫째 줄에 연결 요소의 개수를 출력한다.

* 예제 : 입력                       출력
       --------------------     -----------
        6 5                       2
        1 2
        2 5
        5 1
        3 4
        4 6

        입력                       출력
       --------------------     -----------
        6 8                       1
        1 2
        2 5
        5 1
        3 4
        4 6
        5 4
        2 4
        2 3
        
todo : 1) 정점의 개수 N과 간선의 개수 M을 입력받고 부모 테이블을 초기화하고 자기 자신으로 둔다.
       2) M개의 줄에 간선의 양 끝점 u와 v를 입력받고 u가 v보다 작으면 v번째 인덱스에 u를 넣고 u가 v보다 크면 u번째 인덱스에 v를 넣는다.
       3) 모든연산을 마치고 리스트를 출력한다.
       4) 0번째 인덱스를 제외하고 몇가지의 다른 숫자가 있는지 센다.
'''
import sys


def find_parent(parent, x):  # 특정 노드가 속한 집합을 찾기
    if parent[x] != x:  # 루트 노드를 찾을 때까지 재귀호출
        return find_parent(parent, parent[x])
    return(parent[x])


def union_parent(parent, u, v):  # 두 원소가 속한 집합을 합치기(부모노드 설정)
    u = find_parent(parent, u)
    v = find_parent(parent, v)
    if u < v:
        parent[v] = u
    else:
        parent[u] = v


# 정점의 개수 N과 간선의 개수 M을 입력받는다.
N, M = map(int, sys.stdin.readline().split())
# 부모노드를 초기화한다.
parent = [0]*(N+1)

# 부모를 자기 자신으로 초기화한다.
for i in range(1, N+1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    union_parent(parent, u, v)

parent_list = []
# 부모노드를 리스트에 넣는다.
for a in parent:
    parent_list.append(find_parent(parent, u))

# 중복되는 부모노드를 없애고 0번 인덱스를 제외하고 몇가지의 숫자가 있는지 센다.
Connected_Component = len(set(parent_list))-1

print(Connected_Component)
