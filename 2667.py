'''
작성자 : 서현

작성일자 : 2022.02.21

작성내용 : <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 
단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2
>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

todo :
1) 가로와 세로가 N크기인 정사각형에 한 행씩 입력 받아 행렬을 만든다.
2) dfs를 이용하여 인접한 부분을 찾아 집이 모여 있는 단지의 수를 구한다.
3) dfs를 이용하여 인접한 부분을 찾아 낼 때 집(graph[X][Y] == 1)의 개수를 구한다.
4) 집의 개수의 리스트를 오름차순으로 정렬해 나타낸다.

'''

            
N = int(input())                                  # 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)
house_list=[]

graph = []                                        # N X N 행렬 대입
for _ in range(N):
    graph.append(list(map(int, input())))          

def dfs (X,Y):                                    # dfs 알고리즘
    if X <= -1 or X >= N or Y <= -1 or Y >= N :
        return False
        
    if graph[X][Y] == 1:
        global count                              # count 정의
        graph[X][Y] = 0
        count +=1                                 # 집(1)의 개수 새기
        dfs(X-1, Y)
        dfs(X, Y-1)
        dfs(X+1, Y)
        dfs(X, Y+1)
        return True
    return False

result = 0
count = 0
    
for i in range(N):                              # dfs(i,j) == True 이면 result += 1
    for j in range(N):
        if dfs(i, j) == True:
            house_list.append(count) 
            result += 1
            count = 0

print(result)                                  # 단지의 개수
house_list.sort(reverse=False)                 # 단지 별 집 개수 오름차순 정리
for house in house_list:
    print(house)
