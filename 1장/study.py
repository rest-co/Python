a = [1,2,3,4,5,6]
# 0123인덱스 끝 인덱스는 +1해서 마지막에 입력 
print(a[0:4])
#for if
array = [i for i in range(20) if i % 2==1 ]
print(array)
#2차원 리스트 선언
m=3
n=2
arr = [[0]*m for _ in range(n)]
print(arr)
# 공백기준으로 숫자 입력 받아 리스트
li = list(map(int,input().split()))
print(li)
#람다 표현식
a=[('진욱',100),('윤경',80)]
print(sorted(a,key = lambda x: x[1], reverse =True))
#순열 
from itertools import permutations
data = ['a','b','c']
result = list(permutations(data,3))
print(result)
#조합
from itertools import combinations
result = list(combinations(data,2))
print(result)
#중복 순열 
from itertools import product
data = ['a','b','c']
result = list(product(data,repeat=2))
print(result)
#중복 조합
from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data,2))
print(result)
#count
from collections import count