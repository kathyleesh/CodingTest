'''
작성자 : 서현

작성일자 : 2022.03.28

작성내용 : 
* 입력 : 첫 번째 줄에는 종민이의 영어 이름 A가 주어진다. 두 번째 줄에는 '그녀'의 영어 이름 B가 주어진다.
        A와 B 모두 알파벳 대문자로만 이루어진 길이 2 이상 2000 이하의 문자열이며, 둘의 길이가 같음이 보장된다. 이름 궁합을 볼 때는 A의 첫 글자를 먼저 쓴다고 하자.
* 출력 : 이름 궁합의 결과를 두 자리의 숫자로 출력한다. (십의 자리가 0이어도 두 자리로 출력한다)
* 힌트 : 영어 대문자 알파벳 26개의 획수는 순서대로 3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1 로 정한다.

todo :
1) A와 B를 입력받고 it.chain을 사용하여 배열을 엮어 번갈아 나타내는 방법을 사용한다.
2) 알파벳을 주어진 알파벳 획수로 치환한다.
3) 인접한 숫자끼리 더하는 것을 마지막 결과 값 전까지 반복한다.
4) 마지막 바로 전의 수의 첫번째 수의 일의 자리 수를 십의 자리 수로, 두번째 수의 일의 자리 수를 일의 자리수로 합치면 이름 궁합이 나온다.
'''

import itertools as it

A = input()
B = input()
# 주어진 영어 대문자 알파벳 26개의 획수를 순서대로 리스트화 시킨다.
alphabet = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

# A와 B의 길이가 같다고 가정하였으므로 it.chain을 사용하여 배열을 엮어 번갈아 나타내는 방법 사용이 가능하다.
#여기서 *zip을 해줌으로서 리스트와 튜플로부터 unpack 할 수 있다.
namelist = list(it.chain(*zip(list(A), list(B))))

# 알파벳을 숫자로 치환하기 위해서 아스키코드를 이용한다. 입력된 알파벳의 아스키코드에서 A의 아스키 코드인 65를 빼면 alphabet속 배열의 순서에 맞는 획수를 찾을 수 있다.
# 반복을 통하여 namelist에 있는 모든 알파벳을 획수로 바꾼 다음 alphabetlist에 리스트화한다.
alphabetlist = [alphabet[ord(i) - ord('A')] for i in namelist]

Num = len(A)

# 총 단계는 2*Num-2개로 이루어져있다.
for i in range(2*Num - 2):
    # 단계별로 2*Num - 1 - i개씩 계산이 이루어진다.
    for j in range(2*Num - 1 - i):
        # 인접한 숫자끼리 더하여 리스트에 넣고 이를 i번 반복한다.
        alphabetlist[j] += alphabetlist[j+1]

# 모든 반복이 마치면 alphabetlist[0]와 alphabetlist[1]가 마지막 전 단계의 결과 값이다.
# alphabetlist[0]의 일의 자리 수를 십의 자리 수로, alphabetlist[1]의 일의 자리 수를 일의 자리수로 합치면 이름 궁합이 나온다.
score = ((alphabetlist[0]%10)*10) + (alphabetlist[1]%10)

# "십의 자리가 0이어도 두 자리로 출력한다"를 만족하기 위해서 score을 무조건 두자리 수로 만든다.
print('{0:02d}'.format(score))