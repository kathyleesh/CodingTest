'''
작성자 : 서현

작성일자 : 2022.02.07

작성내용 : 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
        첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
        첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.


todo :
1) 단어를 받았을 때, 알파벳을 하나씩 쪼개어 나타낸다.
2) 모두 다 대문자로 변경한다. (because, 나중에 대문자로 출력해야함)
3) 단어의 알파벳이 dic에 존재하면 1을 더하고 새로운 알파벳이면 1을 부여한다.
4) 가장 많이 사용된 알파벳을 [같은 알파벳 사용 횟수, 알파벳]으로 list화 시킨다.
5) 가장 많이 사용된 알파벳이 두개 이상 존재하는 경우 ?를 출력하므로 list를 한개 더 만들어 max2가 존재하면 ?를 출력시키고 존재하지 않으면 list[1]=알파벳을 출력시킨다.

'''
word = input().upper()          # 단어를 받았을 때, 알파벳을 하나씩 쪼개어 나타내고 대문자로 변경한다. (because, 나중에 대문자로 출력해야함)
dic = {}

for i in word:                  # 단어의 알파벳이 dic에 존재하면 1을 더하고 새로운 알파벳이면 1을 부여한다.
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
max = [0,]                      # 가장 많이 사용된 알파벳을 [같은 알파벳 사용 횟수, 알파벳]으로 list화 시킨다.
max2 = [0,]
for j, i in dic.items():
    if i >= max[0]:
        max2 = max
        max = [i , j]
if max[0] == max2[0]:          # 가장 많이 사용된 알파벳이 두개 이상 존재하는 경우 ?를 출력하므로 list를 한개 더 만들어 max2가 존재하면 ?를 출력시키고 존재하지 않으면 list[1]=알파벳을 출력시킨다.
    print('?')
else:
    print(max[1])

'''
input = input().upper()                                       # 단어를 받았을 때, 알파벳을 하나씩 쪼개어 나타내고 대문자로 변경한다. (because, 나중에 대문자로 출력해야함)
inputlist = list(input)                                       # 단어를 리스트화 한다.
dic = {}

for i in range(len(inputlist)):                               # i가 len(inputlist)의 범위일 때, list안의 단어들을 count해서 dictionary 만든다.
    dic[inputlist[i]] = inputlist.count(inputlist[i])

max = [k for k,v in dic.items() if max(dic.values()) == v]    # value가 Max인 값을 모두 찾아낸다.

if len(max) == 1:                                             # Max 값이 하나이면 그 key값을 출력한다.
    print(max)
else:
    print('?')                                                # Max 값이 두 개 이상이면 '?'를 출력한다.
'''